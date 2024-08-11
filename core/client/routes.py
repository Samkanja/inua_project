from flask import Blueprint, render_template
from core.models import Program

client = Blueprint("client", __name__)


@client.route("/")
def home():
    return render_template("client/home.html")


@client.route("/programs")
def programs():
    programs = Program.query.all()
    return render_template("client/programs.html", programs=programs)
