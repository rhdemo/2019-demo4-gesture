import os


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'flask-api-starter-secret-key')


