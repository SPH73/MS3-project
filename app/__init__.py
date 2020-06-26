import os
from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from flask_ckeditor import CKEditor



app = Flask(__name__)

app.config.from_object(Config)
images = os.environ.get('IMAGES_UPLOADS')
files = os.environ.get('FILE_UPLOADS')
mongo = PyMongo(app)
ckeditor = CKEditor(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
from app import routes