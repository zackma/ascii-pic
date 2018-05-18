# -*- coding:utf-8 -*-

from flask import Flask
from flask_uploads import IMAGES, UploadSet, configure_uploads

from app.mytask import task

app = Flask(__name__)

photos = UploadSet('PHOTO')

app.config['UPLOADED_PHOTO_DEST'] = r'E:/flask_upload'
app.config['UPLOADED_PHOTO_ALLOW'] = IMAGES
# app.config['SCHEDULER_API_ENABLE'] = True

app.register_blueprint(task, url_prefix='/task')

configure_uploads(app, photos)
