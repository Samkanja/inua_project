import os
import secrets
from pathlib import Path
from flask import url_for, current_app
from PIL import Image
from werkzeug.utils import secure_filename


def save_picture(form_picture, location):
    pic_path = os.path.join(str(current_app.static_folder), f"images/{location}")
    if not os.path.exists(pic_path):
        os.mkdir(pic_path)

    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(pic_path, picture_fn)
    # output_size = (125, 125)
    i = Image.open(form_picture)
    # i.thumbnail(output_size)
    i.save(picture_path)
    return f"images/{location}/" + str(picture_fn)


def create_path(location, file):
    pic_path = os.path.join(str(current_app.static_folder), f"images/{location}")
    if not os.path.exists(pic_path):
        os.mkdir(pic_path)
    image_file = secure_filename(file.filename)
    random_string = secrets.token_hex(8)
    _, f_ext = os.path.splitext(image_file)
    picture_fn = random_string + f_ext
    file.save(os.path.join(pic_path, picture_fn))
    return f"images/{location}/" + str(picture_fn)
