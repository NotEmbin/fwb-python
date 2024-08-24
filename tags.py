import glob
import json
from data import registries
from util.log import new_log
from other import path_to_tag_data

print = new_log # NOQA
tags = {}


def load_tags(location=""):
    global tags
    tags = {}
    for reg in registries:
        tag_files = glob.glob(pathname=(location + "data/*/tags/" + reg + "/**/*.json"), recursive=True)
        tag_dict = {}
        for f in tag_files:
            name = path_to_tag_data(f, reg)
            with open(f) as file:
                file_contents = json.load(file)
            try:
                tag_dict[name] = file_contents
                print('Loaded ' + reg + ' tag "' + name + '"')
            except:
                print('Failed to load ' + reg + ' tag "' + name + '"', "error")
        tags[reg] = tag_dict
