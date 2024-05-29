import yaml
from pathlib import Path

ROOT = Path().absolute()
PATH= ROOT / 'core/client'

FILENAME = '_about.yaml'

def read_file():
    web_data =  yaml.load(open(PATH / FILENAME), Loader=yaml.FullLoader)
    return web_data



dic = read_file()
print(dic)
    


