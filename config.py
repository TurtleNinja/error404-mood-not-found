import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or "error404-mood-not-found"
    os.environ['FLASK_ENV'] = "development"
    os.environ['FLASK_DEBUG'] = "1"
    
    # database
    SQLALCHEMY_DATABASE_URI = "postgres://jspwcxkndxkxpo:ddd0d0a15ca2b330a5efa61135d511c0e7aa50c34b04edbacf6989a8b0813f88@ec2-52-205-61-60.compute-1.amazonaws.com:5432/dcbk6ho8t318sh"
    SQLALCHEMY_TRACK_MODIFICATIONS = False