import shutil
from flask import Flask
from core import config_all
from pathlib import Path

# set static directory
if Path(Path(Path.cwd()).parent / "config").exists():
    app_data = Path(Path(Path.cwd()).parent / "config")
    shutil.copytree(Path(Path.cwd()) / "static", app_data, dirs_exist_ok=True)
else:
    app_data = "static"

app = Flask(__name__, static_folder=app_data)
config_all(app)


if __name__ == "__main__":
    app.run(debug=True)
