from flask import Flask
from flask_admin.contrib.sqla import ModelView

from .config import Config
from .extensions import db, bcrypt, login_manage, migrate, admin

from .models.post import Post
from .models.user import User
from .routers.post import post
from .routers.profile import profile
from .routers.auth import register_login
from .routers.main import main


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    app.register_blueprint(register_login, url_prefix="/auth")
    app.register_blueprint(main)
    app.register_blueprint(post, url_prefix="/post")
    app.register_blueprint(profile)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manage.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)

    login_manage.login_view = 'auth_blueprint.register'
    login_manage.login_message = 'Пожалуйста, войдите, чтобы получить доступ к этой странице.'
    login_manage.login_message_category = 'danger'

    with app.app_context():
        db.create_all()


    admin.add_view(ModelView(User, db.session, name="Пользователи"))
    admin.add_view(ModelView(Post, db.session, name="Пост"))

    return app
