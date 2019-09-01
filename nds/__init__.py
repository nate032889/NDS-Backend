from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config=Config):
    """
    Function to initialize the web app
    :param config: Config class
    :return: initialized application
    """

    app = Flask(__name__)
    app.config.from_object(config)

    # init db with app instance
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from nds.main.routes import main
    app.register_blueprint(main)
    
    return app
