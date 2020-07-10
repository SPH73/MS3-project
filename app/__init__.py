import os
from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from flask_ckeditor import CKEditor
from filters import datetimeformat


app = Flask(__name__)
app.config.from_object(Config)
ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg']
ALLOWED_FILE_EXTENSIONS = ['txt', 'pdf']
MAX_IMAGE_SIZE = 5 * 1024 ** 2

mongo = PyMongo(app)
ckeditor = CKEditor(app)

app.jinja_env.filters['datetimeformat'] = datetimeformat

from app import routes