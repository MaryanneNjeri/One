from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
# Creating the instances
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
#creating the app instance
    app =Flask(__name__)
#importing the  configurations directly to the application
    app.config.from_object(config_options[config_name])
#intialzing the extensions
    bootstrap.init_app(app)
    db.init_app(app)
#importing the instance main
    from .main import main as main_blueprint
#then register the blueprint
    app.register_blueprint(main_blueprint)
    from .request import configure_request
    configure_request(app)

    return app
