from flask import Blueprint, render_template


client_views = Blueprint('client',__name__)


@client_views.route("/")
def home():
    return render_template('home.html')