import yaml
import os
from config import BASE_URL
def resd_yaml(filename):
    with open(BASE_URL + os.sep + "data" + os.sep + filename,"r",encoding="utf-8") as f:
        arr = []
        for data in yaml.load(f).values():
            arr.append(tuple(data.values()))
        return arr

