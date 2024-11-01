from datetime import datetime
from ..extensions import db

class Base:
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, default=datetime.now)
