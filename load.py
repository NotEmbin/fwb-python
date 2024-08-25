import json
from better_log import log
from textures import load_textures
from data import load_registries
from tags import load_tags

print = log.new_log # NOQA

resource_packs = []
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

    print(selected_resource_packs)
