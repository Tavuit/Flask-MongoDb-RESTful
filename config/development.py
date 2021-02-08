# coding: utf-8
import os
class DevelopmentConfig(object):
    """Base config class."""
    # Flask app config
    DEBUG = True
    TESTING = False
    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # MongoEngine config
    MONGODB_SETTINGS = {
        'db': 'todo',
        'host': 'localhost',
        'port': 27017
    }
    JWT_SECRET_KEY = 'TODO_RESTFull_API'
    JWT_ACCESS_TOKEN_EXPIRES = 3600