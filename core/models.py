import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import UserMixin

db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(admin_id)

def generate_uuid():
    return str(uuid.uuid4())

class Admin(db.Model, UserMixin):
    id = db.Column(db.String(30), primary_key=True,default=generate_uuid)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"Admin({self.username})"


class Program(db.Model):
    id = db.Column(db.String(30), primary_key=True, default=generate_uuid)
    title = db.Column(db.String(120),nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)
    picture = db.Column(db.String(120), nullable=False,default='default.jpg')