import os
from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from flask_ckeditor import CKEditor


app = Flask(__name__)
app.config.from_object(Config)
ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg']
ALLOWED_FILE_EXTENSIONS = ['txt']
MAX_IMAGE_SIZE = 5 * 1024 ** 2
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

mongo = PyMongo(app)
ckeditor = CKEditor(app)

from app import routes