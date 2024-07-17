import os
import re
from flask import Blueprint, render_template, redirect, url_for,flash, request
from core.admin.forms import AdminRegistrationForm, LoginForm, ProgramForm
from core.models import Admin, db, Program
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user, login_required,logout_user



admin_views = Blueprint("admin", __name__)

bcrypt = Bcrypt()

@admin_views.route('/admin')
def admin_home():
    return render_template("admin/home.html")


@admin_views.route("/admin/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('admin.admin_home'))
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        if Admin.query.count() < 1:
            admin = Admin(username=form.username.data, password=hashed_password)
            db.session.add(admin)
            db.session.commit()
            flash("Your account has been created! You are now able to log in",'success')
            return redirect(url_for("admin.admin_home"))
    return render_template("admin/register.html",title='register',form=form)


@admin_views.route("/admin/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.admin_home'))
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin.admin_home'))
        else:
            flash("Login Unsuccessfull. Please check username and password", "danger")
    return render_template('admin/login.html', title='login',form=form)


@admin_views.route("/admin/logout")
def logout():
    logout_user()
    return redirect(url_for("admin.login"))


@admin_views.route("/admin/program", methods=["GET", "POST"])
def create_program():
    form = ProgramForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = secure_filename(form.picture.filename)
            picture.save(os.path.join(app.config['UPLOAD_FOLDER'], picture_file))
        else:
            picture_file = None
            
        program = Program(title=form.title.data,description=form.description.data,picture=form.picture.data)
        db.session.add(program)
        db.session.commit()
        flash("Your program has been created",'success')
        return redirect(url_for('admin.admin_home'))
    # image_file = url_for('static', filename='program_imgs/' + program.picture)
    return render_template('admin/program.html', form=form,title='program')


def secure_filename(filename):
    # Replace spaces with underscores
    filename = filename.replace(' ', '_')
    
    # Remove non-alphanumeric characters, except for '.', '_', '-'
    filename = re.sub(r'[^\w.-]', '', filename)
    
    # Remove leading and trailing separators and dots
    filename = filename.strip('._-')
    
    # Ensure filename is not empty after stripping
    if not filename:
        raise ValueError('Invalid filename')
    
    return filename

# def save_picture(form_picture):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_picture)
#     picture_fn = random_hex + f_ext
#     picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

#     output_size = (125, 125)
#     i = Image.open(form_picture)
#     i.thumbnail(output_size)
#     i.save(picture_path)

#     return picture_fn