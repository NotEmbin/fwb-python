import pygame
import glob
import json
from better_log import log
from other import path_to_assets
from other import to_namespace

pygame.init()
print = log.new_log # NOQA

texture_dict = {}


def get_texture(texture, width: int, height: int):
    texture_id = to_namespace(texture)
    try:
        used_texture = texture_dict[texture_id]
    except KeyError:
        used_texture = texture_dict[to_namespace("fallback")]
    used_texture = pygame.transform.scale(used_texture, (width, height))
    return used_texture.convert_alpha()


def load_textures(full_reload: bool = True, location: str = "", dump: bool = False):
    global texture_dict
    if full_reload:
        texture_dict = {}
    texture_files = glob.glob(pathname=location + "assets/*/textures/**/*.png", recursive=True)
    for txt in texture_files:
        name = path_to_assets(txt)
        texture_dict[name] = pygame.image.load(txt)
        print('Loaded texture "' + name + '"')
    if dump:
        texture_keys = dict()
        texture_keys["loaded_textures"] = list(texture_dict.keys())
        with open("dumps/textures.json", "w") as f:
            f.write(json.dumps(texture_keys, indent=2))
