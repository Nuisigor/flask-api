import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Environment:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.getenv('DATABASE_DIR', 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False').lower() in ['true', '1', 't']
    DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't']
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    API_KEY = os.getenv('API_KEY')

