from flask import Blueprint

register_login = Blueprint('auth_blueprint', __name__)
post = Blueprint('post_blueprint', __name__)
profile = Blueprint('profile_blueprint', __name__)
main = Blueprint('main_blueprint', __name__)

