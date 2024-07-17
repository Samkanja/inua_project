import yaml
from .play import read_file, read_json
from flask import Blueprint, render_template
from pathlib import Path
from core.models import Program

ROOT = Path().absolute()
PATH= ROOT / 'core/client'

FILENAME = '_about.yaml'
FILENAME1 = "_program.json"

client_views = Blueprint("client", __name__)

abouts = read_file(PATH/FILENAME)

df = read_json(PATH/ FILENAME1)
print(df)
# programs = [
#     {"title" : "Here To stay", "desc":"jdkfdjsjfkdsfdlfldsfkldsfldkfdlkfdlkfldkfldkklfklfkdlfklfkglfkglf"},
#     {"title": "antiert ", "desc": "jdkfdjsjfkdsfdlfldsfkldsfldkfdlkfdlkfldkfldkklfklfkdlfklfkglfkglf"},
#     {"title":"jdskfjkadjfksd","desc":"jdkfdjsjfkdsfdlfldsfkldsfldkfdlkfdlkfldkfldkklfklfkdlfklfkglfkglf"}
# ]

@client_views.route("/")
def home():
    return render_template("home.html")


@client_views.route("/about")
def about_us():
    return render_template("about.html", abouts=abouts)


@client_views.route("/programs")
def program():
        programs = Program.query.all()
        return render_template("programs.html", programs=programs)
