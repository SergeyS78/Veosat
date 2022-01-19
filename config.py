"""Config for Flask application"""

import os
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))


class Config(object):
    """Settings for run Flask application"""

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # database settings
    # for mysql is used file .env in form:
    #   DATABASE_URL = mysql+pymysql://root:pass@localhost/mydb
    # If DATABASE_URL don't set, by default will be used sqlite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(BASEDIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True
    # SQLALCHEMY_POOL_SIZE = 6
    # SQLALCHEMY_MAX_OVERFLOW = 10


class TestConfig(Config):
    """For test mode"""
    TESTING = True
