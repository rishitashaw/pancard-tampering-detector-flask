import os 
from os import environ

class Config(object):
    DEBUG = False
    TESTING = False

    base_dir = os.path.abspath(os.path.dirname(__file__))
    SECRE_KEY = ''

    UPLOADS = 'C:/Users/rishi/Desktop/programs/flask/pancard-tampering/app/static/uploads'

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class DebugConfig(Config):
    DEBUG = False