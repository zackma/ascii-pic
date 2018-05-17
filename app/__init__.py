# -*- coding:utf-8 -*-
import os
from flask import Flask
from flask_uploads import IMAGES, UploadSet, configure_uploads

app = Flask(__name__)

photos = UploadSet('PHOTO')

app.config['UPLOADED_PHOTO_DEST'] = r'E:/flask_upload'
app.config['UPLOADED_PHOTO_ALLOW'] = IMAGES

configure_uploads(app, photos)
