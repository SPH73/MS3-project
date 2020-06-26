import os

class Config(object):
    
    # Flask config
    SECRET_KEY  = os.environ.get('SECRET_KEY')
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_OPTIONS = {'theme': 'white'}
    
    #  Database
    MONGO_URI = os.environ.get('MONGO_URI')
    MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
    MONGODB_SETTINGS = {
        'DB': 'codeflow',
        'host': 'localhost',
        'port': 27017
    }
    
    # Uploads
    
    IMAGE_UPLOADS_ = os.environ.get('IMAGE_UPLOADS')
   
    FILE_UPLOADS = os.environ.get('FILE_UPLOADS')
   
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}