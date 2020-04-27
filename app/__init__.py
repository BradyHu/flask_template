from flask import Flask
from flask_cors import CORS

def register_blueprints(app):
    """
    此函数用于将redprint注册到blueprint
    :param app:
    :return:
    """
    from app.api import blueprint as api
    app.register_blueprint(api)


def register_plugin(app):
    CORS(app)
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all(app=app)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.settings')  # 明文变量
    app.config.from_object("app.config.secure")  # 密文变量
    register_blueprints(app)
    register_plugin(app)
    return app