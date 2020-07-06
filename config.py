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
    
    IMAGE_UPLOADS = os.environ.get('IMAGE_UPLOADS')
   
    FILE_UPLOADS = os.environ.get('FILE_UPLOADS')


S3_BUCKET = os.environ.get('S3_BUCKET') 
S3_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
S3_SECRET = os.environ.get('AWS_SECRET_ACCESS_KEY')