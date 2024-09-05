import json
import logging
from os import path
from textures import load_textures
from data import load_registries
from tags import load_tags

logging.basicConfig(format="[%(asctime)s] [%(levelname)s] %(message)s", level=logging.DEBUG)

resource_packs = [] # TODO: rename to "available_resource_packs"
selected_resource_packs = []


def load_resources(include_resource_packs: bool = True):
    global resource_packs
    global selected_resource_packs
    load_registries()
    load_tags()
    load_textures()

    if include_resource_packs:
        with open("settings.json", "r") as f:
            selected_resource_packs = json.load(f)["resource_packs"]

        for rp in selected_resource_packs:
            rppath = "resourcepacks/" + rp + "/"
            packjsonpath = rppath + "pack.json"
            pack_exists = path.isfile(packjsonpath)
            if pack_exists:
                try:
                    logging.info('Loading resource pack "' + rp + '"')
                    with open(packjsonpath, "r") as ff:
                        pack_json = json.load(ff)
                    load_registries(location=rppath, full_reload=False)
                    load_tags(location=rppath, full_reload=False)
                    load_textures(location=rppath, full_reload=False)
                except FileNotFoundError as e:
                    logging.exception(f'File not found error: {e}')
                except Exception as e:
                    logging.exception(f'An error occurred when loading the resource pack "{rp}": {e}')
            else:
                logging.warning('Selected pack "' + rp + '" does not exist, or does not have a "pack.json" file!')

    logging.info(selected_resource_packs)
