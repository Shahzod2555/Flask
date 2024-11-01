from ..extensions import db, bcrypt
from ..models.user import User
from flask import redirect, render_template, request, flash, url_for
from ..forms.user import RegisterForm, SignInForm
from flask_login import login_user, login_required, logout_user
from flask import Blueprint

register_sign_up = Blueprint('register_sign_in_blueprint', __name__)

@register_sign_up.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        login = form.login.data
        email = form.email.data
        password = form.password.data

        if User.query.filter_by(email=email).first():
            flash("Этот email уже зарегистрирован.", "danger")
            return redirect(request.referrer or url_for('main_blueprint.index'))

        if User.query.filter_by(username=login).first():
            flash("Этот логин уже зарегистрирован.", "danger")
            return redirect(request.referrer or url_for('main_blueprint.index'))

        else:
            hash_pwd = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(username=login, password_hash=hash_pwd, email=email)
            try:
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                flash("Вы успешно зарегистрировались", "success")
                return redirect(url_for('main_blueprint.index'))
            except Exception as e:
                db.session.rollback()
                print(e)
                flash("Что-то пошло не так попробуйте позже", "danger")
                return redirect(request.referrer or url_for('main_blueprint.index'))
    return render_template('authorization/register.html', form=form, title="Зарегистрироваться")


@register_sign_up.route('/login', methods=['GET', 'POST'])
def sign_in():
    form = SignInForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.data["login"]
        password = form.data["password"]

        if username and password:
            user = User.query.filter_by(username=username).first()

            if user and bcrypt.check_password_hash(user.password_hash, password):
                login_user(user)
                flash("Вы успешно вошли в свой аккаунт", "success")
                return redirect(url_for('main_blueprint.index'))
            else:
                flash('Неверный логин или пароль', "danger")
                return redirect(request.referrer)
        else:
            flash('Пожалуйста, введите логин и пароль', "danger")
            return redirect(request.referrer)

    return render_template(template_name_or_list='authorization/sign_in.html', form=form, title="Вход")


@register_sign_up.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')