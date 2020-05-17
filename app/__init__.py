import os
from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt




app = Flask(__name__)

app.config.from_object(Config)

mongo = PyMongo(app)
bcrypt = Bcrypt(app)


from app import routes

