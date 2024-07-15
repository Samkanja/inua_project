from flask import Blueprint, render_template, redirect, url_for,flash, request
from core.admin.forms import AdminRegistrationForm, LoginForm
from core.models import Admin, db
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user, login_required,logout_user



admin_views = Blueprint("admin", __name__)

bcrypt = Bcrypt()

@admin_views.route('/admin/home')
def home():
    return render_template("admin/home.html")


@admin_views.route("/admin", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('admin.home'))
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        if Admin.query.count() < 1:
            admin = Admin(username=form.username.data, password=hashed_password)
            db.session.add(admin)
            db.session.commit()
            flash("Your account has been created! You are now able to log in",'success')
            return redirect(url_for("admin.home"))
    return render_template("admin/register.html",title='register',form=form)


@admin_views.route("/admin/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.home'))
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin.home'))
        else:
            flash("Login Unsuccessfull. Please check username and password", "danger")
    return render_template('admin/login.html', title='login',form=form)


@admin_views.route("/admin/logout")
def logout():
    logout_user()
    return redirect(url_for("admin.login"))