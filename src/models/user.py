from flask_login import UserMixin
from .base_model import Base
from ..extensions import db, login_manage


@login_manage.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, Base, UserMixin):
    __tablename__ = 'user'
    username = db.Column(db.Text, unique=True)
    admin = db.Column(db.Boolean, default=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password_hash = db.Column(db.Text)

    posts = db.relationship("Post", back_populates="author", cascade="all, delete-orphan", lazy=True)

    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash
