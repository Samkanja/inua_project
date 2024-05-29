import yaml
from .play import read_file
from flask import Blueprint, render_template



client_views = Blueprint('client',__name__)

web_data = read_file()

@client_views.route("/")
def home():
    return render_template('home.html')


@client_views.route("/about")
def about_us():
    
    return render_template('about.html', abouts=web_data)





