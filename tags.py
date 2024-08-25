import glob
import json
from data import registries
from better_log.log import new_log
from other import path_to_tag_data
from other import flatten

print = new_log # NOQA
tags = {}

# print('The ' + reg + ' tag ' + tag + ' references ' + s + ', so that tag\'s contents will be merged into ' + tag, "tag")  # NOQA


def load_tags(full_reload: bool = True, location: str = "", dump: bool = False):
    global tags
    if full_reload:
        tags = {}
        for _ in registries:
            tags[_] = {}
    for reg in registries:
        tag_files = glob.glob(pathname=(location + "data/*/tags/" + reg + "/**/*.json"), recursive=True)
        tag_dict = tags[reg]
        for f in tag_files:
            name = path_to_tag_data(f, reg)
            with open(f) as file:
                file_contents = json.load(file)
            replace = False
            if "name" in tag_dict:
                if "replace" in file_contents:
                    replace = file_contents["replace"]
                else:
                    replace = False
            try:
                if name not in tag_dict:
                    replace = True
                if replace:
                    tag_dict[name] = file_contents["data"]
                else:
                    tag_dict[name] = (tag_dict[name] + file_contents["data"])
                print('Loaded ' + reg + ' tag "' + name + '"')
            except:
                print('Failed to load ' + reg + ' tag "' + name + '"', "error")
        tags[reg] = tag_dict

        # replace references to other tags with the contents of the referenced tag
        while True:
            if "#" not in str(tag_dict):
                break
            for tag in tag_dict:
                for i, s in enumerate(tag_dict[tag]):
                    if s.startswith("#"):
                        tag_dict[tag][i] = tag_dict[s.replace("#", "", 1)]
                tag_dict[tag] = flatten(tag_dict[tag])
    if dump:
        with open("dumps/tags.json", "w") as f:
            f.write(json.dumps(tags, indent=2))
