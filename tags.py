import glob
import json
import logging
from data import registries
from other import path_to_tag_data
from other import flatten
from other import to_namespace

logging.basicConfig(format="[%(asctime)s] [%(levelname)s] %(message)s", level=logging.DEBUG)
tags = {}

# print('The ' + reg + ' tag ' + tag + ' references ' + s + ', so that tag\'s contents will be merged into ' + tag, "tag")  # NOQA


def get_tag(registry: str, tag_name: str):
    global tags
    try:
        return tags[registry, to_namespace(tag_name)]
    except KeyError as e:
        logging.exception(f'Unknown key(s) {e} when trying to get contents of {registry} tag "{to_namespace(tag_name)}"', "error")
        return []


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
            name = path_to_tag_data(f, reg, location)
            try:
                with open(f) as file:
                    file_contents = json.load(file)
                replace = False
                if "name" in tag_dict:
                    if "replace" in file_contents:
                        replace = file_contents["replace"]
                    else:
                        replace = False
                if name not in tag_dict:
                    replace = True
                if replace:
                    tag_dict[name] = file_contents["data"]
                else:
                    tag_dict[name] = (tag_dict[name] + file_contents["data"])
                logging.info('Loaded ' + reg + ' tag "' + name + '"')
            except KeyError as e:
                logging.exception(f'The {reg} tag "{name}" does not contain an expected key: {e}')
            except Exception as e:
                logging.exception('Failed to load ' + reg + ' tag "' + name + '" due to error: ' + e)
        tags[reg] = tag_dict

        # replace references to other tags with the contents of the referenced tag
        while True:
            if "#" not in str(tag_dict):
                break
            for tag in tag_dict:
                for i, tag_name in enumerate(tag_dict[tag]):
                    if tag_name.startswith("#"):
                        try:
                            tag_dict[tag][i] = tag_dict[tag_name.replace("#", "", 1)]
                        except KeyError as e:
                            logging.error(f'The {reg} tag "{tag}" references unknown tag "{tag_name}": {e}')
                            tag_dict[tag][i] = "uh oh"
                        except Exception as e:
                            logging.error(f'An error occurred when resolving tag references in the {reg} tag "{tag}": {e}')
                            tag_dict[tag][i] = []
                tag_dict[tag] = flatten(tag_dict[tag])
    logging.debug(tags)
    if dump:
        with open("dumps/tags.json", "w") as f:
            f.write(json.dumps(tags, indent=2))
