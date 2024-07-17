from flask import Flask
from core import config_all



app = Flask(__name__)
config_all(app)


if __name__ == '__main__':
    app.run(debug=False)
