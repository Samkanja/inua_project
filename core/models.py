import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from flask_login import LoginManager, UserMixin


db = SQLAlchemy()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(admin_id):
    try:
        return Admin.query.get(admin_id)
    except OperationalError:
        return None


def generate_uuid():
    return str(uuid.uuid4())


class Admin(db.Model, UserMixin):
    id = db.Column(db.String(30), primary_key=True, default=generate_uuid)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    programs = db.relationship("Program", backref="admin", lazy=True)

    def __repr__(self):
        return f"Admin({self.username})"


class Program(db.Model):
    id = db.Column(db.String(30), primary_key=True, default=generate_uuid)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(255), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"), nullable=False)

    def __repr__(self):
        return f"Program({self.title})"
