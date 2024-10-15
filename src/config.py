import os

class Config:
    # General Config
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    DEBUG = os.getenv('DEBUG', False) == 'True'
    TESTING = os.getenv('TESTING', False) == 'True'

    #Database Config for Heroku postgres
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///userdata.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False