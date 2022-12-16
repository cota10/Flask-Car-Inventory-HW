import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

 

class Config():
    """
        Set Config variables for the flask app.
        Using Environment variables where available otherwise
        create the config variable if not done already.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or ('New secret key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False