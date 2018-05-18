# -*- coding:utf-8 -*-
import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from flask import Blueprint

task = Blueprint('task', __name__)


@task.route('/')
def work():
    '''关于APSCHEDULER时间表达式的例子
       （1）cron定时调度（某一定时时刻执行）
       #表示2017年3月22日17时19分07秒执行该程序
       schedudler.add_job(my_job, 'cron', year=2017,month = 03,day = 22,hour = 17,minute = 19,second = 07)

       #表示任务在6,7,8,11,12月份的第三个星期五的00:00,01:00,02:00,03:00 执行该程序
       schedudler.add_job(my_job, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')

       #表示从星期一到星期五5:30（AM）直到2014-05-30 00:00:00
       schedudler.add_job(my_job(), 'cron', day_of_week='mon-fri', hour=5, minute=30,end_date='2014-05-30')

       #表示每5秒执行该程序一次，相当于interval 间隔调度中seconds = 5
       schedudler.add_job(my_job, 'cron',second = '*/5')

       （2）interval 间隔调度（每隔多久执行）
       #表示每隔3天17时19分07秒执行一次任务
       schedudler.add_job(my_job, 'interval',days  = 03,hours = 17,minutes = 19,seconds = 07)

       （3）date 定时调度（作业只会执行一次）
       # The job will be executed on November 6th, 2009
       schedudler.add_job(my_job, 'date', run_date=date(2009, 11, 6), args=['text'])
       # The job will be executed on November 6th, 2009 at 16:30:05
       schedudler.add_job(my_job, 'date', run_date=datetime(2009, 11, 6, 16, 30, 5), args=['text'])
    '''
    schedudler = BlockingScheduler()
    schedudler.add_job(job, 'cron', second='*/5')
    schedudler.start()


def job():
    print("hello scheduler——" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
