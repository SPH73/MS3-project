import os
from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from flask_ckeditor import CKEditor



app = Flask(__name__)

app.config.from_object(Config)

mongo = PyMongo(app)

ckeditor = CKEditor(app)



from app import routes

