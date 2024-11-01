from ..extensions import db
from ..forms.post import CreatePostForm
from ..models.post import Post
from flask import redirect, render_template, request, url_for, flash, abort
from . import post
from flask_login import current_user, login_required


@post.route('/create/post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = CreatePostForm()
    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_post = Post(title=title, content=content, author_id=current_user.id)
        try:
            db.session.add(new_post)
            db.session.commit()
            flash("Поздравляю новый пост успешно создан", "success")
            return redirect(request.referrer or url_for('main_blueprint.index'))
        except Exception as e:
            db.session.rollback()
            print(e)
            flash("Что-то пошло не так попробуйте позже")
            return redirect(request.referrer or url_for('main_blueprint.index'))
    return render_template(template_name_or_list='post/create_post.html', form=form, title="fdwef")


@post.route('/delete/post/<int:id_post>', methods=['POST'])
@login_required
def delete_post(id_post):
    post_to_delete = Post.query.get(id_post)
    if post_to_delete is None:
        abort(404, description="Post not found")

    if post_to_delete.author_id == current_user.id:
        try:
            db.session.delete(post_to_delete)
            db.session.commit()
            flash("Пост успешно удален.", "success")
            return redirect(request.referrer or url_for('main_blueprint.index'))
        except Exception as e:
            db.session.rollback()
            print(e)
            flash("Что-то пошло не так попробуйте позже")
            return redirect(request.referrer or url_for('main_blueprint.index'))
    elif post_to_delete.author_id != current_user.id:
        flash("Ой иди ты в жопу это не твой пост че ты его удаляешь?", "danger")
        return redirect(request.referrer or url_for('main_blueprint.index'))
    else:
        flash("Что-то пошло не так попробуйте позже")
        return redirect(request.referrer or url_for('main_blueprint.index'))

