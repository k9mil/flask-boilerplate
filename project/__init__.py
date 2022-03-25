from flask import Flask
from project.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from project.main.routes import main
    from project.errors.routes import errors

    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app