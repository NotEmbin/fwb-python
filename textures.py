import pygame
import glob
from util import log
from other import path_to_assets
from other import to_namespace

pygame.init()
print = log.new_log # NOQA

texture_dict = {}
texture_width = {}
texture_height = {}

texture_files = glob.glob(pathname="assets/*/textures/**/*.png", recursive=True)


def get_texture(texture, width: int, height: int):
    texture_id = to_namespace(texture)
    try:
        used_texture = texture_dict[texture_id]
    except KeyError:
        used_texture = texture_dict[to_namespace("fallback")]
    used_texture = pygame.transform.scale(used_texture, (width, height))
    return used_texture.convert_alpha()


for txt in texture_files:
    name = path_to_assets(txt)
    texture_dict[name] = pygame.image.load(txt)
    texture_width[name] = texture_dict[name].get_width()
    texture_height[name] = texture_dict[name].get_height()
    print('Loaded texture "' + name + '"')
