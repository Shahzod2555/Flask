from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_admin import Admin

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manage = LoginManager()
migrate = Migrate()
admin = Admin(name='MyAdmin', template_mode='bootstrap4')
