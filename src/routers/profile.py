from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from . import profile
from ..extensions import db
from ..models.post import Post
from ..models.user import User


@profile.route('/profile', defaults={'user_id': None}, methods=['GET'])
@profile.route('/profile/<int:user_id>', methods=['GET'])
def profile_page(user_id):
    if user_id is None:
        user_id=current_user.id

    user = User.query.filter_by(id=user_id).first()

    if user is None:
        return redirect(request.referrer or url_for('main_blueprint.index'))

    user_posts = Post.query.order_by(Post.create_date.desc()).filter_by(author_id=user_id).all()

    return render_template(
        template_name_or_list="profile.html",
        user_posts=user_posts,
        user=user
    )


@profile.route('/delete/account')
@login_required
def delete_account():
    try:
        account = User.query.filter_by(id=current_user.id).first()
        db.session.delete(account)
        db.session.commit()
        flash("Аккаунт успешно удален.", "success")
        return redirect(url_for('main_blueprint.index'))
    except Exception as e:
        db.session.rollback()
        print(e)
        flash("Что-то пошло не так попробуйте позже")
        return redirect(request.referrer or url_for('main_blueprint.index'))
