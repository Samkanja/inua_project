import os
import secrets
from flask import (
    Blueprint,
    current_app,
    request,
    render_template,
    url_for,
    redirect,
    flash,
)
from core.models import Admin, db, Program
from .forms import RegistrationForm, LoginForm, ProgramForm
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user, login_required
from .utils import create_path, save_picture
from werkzeug.utils import secure_filename


bcrypt = Bcrypt()

admins = Blueprint("admins", __name__)


@admins.route("/inua")
def admin_home():
    return render_template("admin/inua_home.html")


@admins.route("/inua/register", methods=["GET", "POST"])
def admin_register():
    if current_user.is_authenticated:
        return redirect(url_for("admins.admin_home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        admin = Admin(username=form.username.data, password=hash_password)
        db.session.add(admin)
        db.session.commit()
        flash("Your account has been created! You are now able to log in", "success")
        return redirect(url_for("admins.admin_home"))
    return render_template("admin/register.html", form=form)


@admins.route("/inua/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admins.admin_chome"))
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin)
            next_page = request.args.get("next")
            return (
                redirect(next_page)
                if next_page
                else redirect(url_for("admins.admin_home"))
            )
        else:
            flash("Login Unsuccessfull. Please check username and password", "danger")
    return render_template("admin/login.html", title="login", form=form)


@admins.route("/inua/program", methods=["GET", "POST"])
@login_required
def create_program():
    form = ProgramForm()
    if request.method == "POST":
        file = request.files["program_image"]
        if file:
            image_file = create_path("programs", file)
            program = Program(
                title=form.title.data,
                content=form.content.data,
                image_file=image_file,
                admin=current_user,
            )
            db.session.add(program)
            db.session.commit()
            return redirect(url_for("admins.admin_home"))

    return render_template("admin/program.html", form=form, title="program")
