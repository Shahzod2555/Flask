from .base_model import Base
from ..extensions import db


class Post(db.Model, Base):
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, unique=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    author = db.relationship("User", backref="posts", lazy=True)

    def __init__(self, title, content, author_id):
        self.title = title
        self.author_id = author_id
        self.content = content
