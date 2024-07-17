import yaml
import json
from pathlib import Path

ROOT = Path().absolute()
PATH= ROOT / 'core/client'

FILENAME = '_about.yaml'
FILENAME1 = "_program.json"

def read_file(file_path):
    web_data =  yaml.load(open(file_path), Loader=yaml.FullLoader)
    return web_data



dic = read_file(PATH / FILENAME1)

def read_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
        return data

res = read_json(PATH/ FILENAME1)
 


