import yaml
from flask import Blueprint, render_template

def read_file():
    web_data =  yaml.load(open('core\client\_about.yaml'), Loader=yaml.FullLoader)
    return web_data

client_views = Blueprint('client',__name__)



@client_views.route("/")
def home():
    return render_template('home.html')


@client_views.route("/about")
def about_us():
    web_data =  read_file()
    return render_template('about.html', abouts=web_data)





