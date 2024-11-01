from flask import render_template
from . import main
from ..models.post import Post
from ..models.user import User


@main.route('/', methods=['GET'])
def index():
    users = User.query.all()
    posts = Post.query.all()
    print(f"{len(users)} user")
    print(f"{len(posts)} post")
    return render_template(
        template_name_or_list="main.html",
        title="Главная страница",
        posts=Post.query.order_by(Post.create_date.desc()).all()
    )
