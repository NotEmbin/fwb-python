import json
from os import path
from better_log import log
from textures import load_textures
from data import load_registries
from tags import load_tags

print = log.new_log # NOQA

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
                    print('Loading resource pack "' + rp + '"')
                    with open(packjsonpath, "r") as ff:
                        pack_json = json.load(ff)
                    print(pack_json)
                    load_registries(location=rppath, full_reload=False)
                    load_tags(location=rppath, full_reload=False)
                    load_textures(location=rppath, full_reload=False)
                except FileNotFoundError as e:
                    print(f'File not found error: {e}', "error")
                except Exception as e:
                    print("An error occurred when loading the resource pack \"" + rp + "\", " + e, "error")
            else:
                print('Selected pack "' + rp + '" does not exist, or does not have a "pack.json" file!', "warn")

    print(selected_resource_packs)
