from os import environ, path
from dotenv import load_dotenv

# Specificy a `.env` file containing key/value config values
#Se obtiene la ruta absoluta del archivo donde se está ejecutando el código usando file y path.abspath y path.dirname
file_dir = path.abspath(path.dirname(__file__))
#Tambien se obtiene la ruta del directorio raíz usando path.dirname sobre la ruta del paso anterior.
root_dir = path.dirname(file_dir)
#root_dir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(root_dir, '.env'))

class Config:
    """Base config."""
    #obtiene el valor de la variable SECRET_KEY declarada en el .env
    SECRET_KEY = environ.get('SECRET_KEY')
    #arma la ruta de la base de datos sqlite usando la ruta raíz y el valor de la variable SQLITE_FILE_RELATIVE_PATH del .env
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(root_dir, environ.get('SQLITE_FILE_RELATIVE_PATH'))

'''
class Config:
    ENVIRONMENT = environ.get("ENVIRONMENT")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
'''
