import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or "error404-mood-not-found"
    os.environ['FLASK_ENV'] = "development"
    os.environ['FLASK_DEBUG'] = "1"
    
    # database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False