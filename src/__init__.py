from flask import Flask
from .config import Config
from .extensions import db, bcrypt, login_manage
from .routers.post import post
from .routers.profile import profile
from .routers.sign_up_in import register_sign_up
from .routers.main import main

def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(register_sign_up)
    app.register_blueprint(main)
    app.register_blueprint(post)
    app.register_blueprint(profile)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manage.init_app(app)

    login_manage.login_view = 'register_sign_in_blueprint.register'
    login_manage.login_message = 'Пожалуйста, войдите, чтобы получить доступ к этой странице.'
    login_manage.login_message_category = 'danger'

    with app.app_context():
        db.create_all()

    return app
