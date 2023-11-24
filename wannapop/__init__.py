from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

db_manager = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # Construct the core app object
    app = Flask(__name__)
    app.config.from_object('wannapop.config.Config')
    # Using a production configuration
    # app.config.from_object('config.ProdConfig')

    # Using a development configuration
    #app.config.from_object('config.DevConfig')

    # Secret key
    ##app.config["SECRET_KEY"] = "Valor aleatori molt llarg i super secret"

    # ruta absoluta d'aquesta carpeta
    #basedir = os.path.abspath(os.path.dirname(__file__)) 

    # paràmetre que farà servir SQLAlchemy per a connectar-se
    ##app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + basedir + "/../database.db"
    # mostre als logs les ordres SQL que s'executen
    #app.config["SQLALCHEMY_ECHO"] = True

    # Inicialitza els plugins
    login_manager.init_app(app)
    db_manager.init_app(app)

    with app.app_context():
        from . import routes_main, routes_auth

        # Registra els blueprints
        app.register_blueprint(routes_main.main_bp)
        app.register_blueprint(routes_auth.auth_bp)

    app.logger.info("Aplicació iniciada")
    #app.logger.debug(app.config)

    return app