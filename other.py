import pygame
from better_log import log

pygame.init()
print = log.new_log # NOQA

game_version = 1
game_version_display = "1.0.0"
game_id = "fwb"
game_name = "FNAF World Battle" # NOQA
font = pygame.font.Font("assets/fwb/font/minecraft.ttf", 24)


def to_namespace(string):
    s = string.lower()
    if ":" not in s:
        s = game_id + ":" + s
    return s


def replace_last(string, old, new, count):
    return new.join(string.rsplit(old, count))


def assets_path(path):
    s = path.replace(":", "/textures/", 1)
    return "assets/" + s + ".png"


def path_to_assets(path):
    s = path.replace("assets\\", "", 1)
    s = s.replace("\\textures\\", ":", 1)
    s = s.replace("\\", "/")
    s = replace_last(s, ".png", "", 1)
    return s


def data_path(path):
    s = path.replace(":", "/", 1)
    return "data/" + s + ".json"


def path_to_data(path, reg):
    s = path.replace("data\\", "", 1)
    s = s.replace("\\" + reg + "\\", ":", 1)
    s = s.replace("\\", "/")
    s = replace_last(s, ".json", "", 1)
    return s


def path_to_tag_data(path, reg):
    s = path.replace("data\\", "", 1)
    s = s.replace("\\tags\\" + reg + "\\", ":", 1)
    s = s.replace("\\", "/")
    s = replace_last(s, ".json", "", 1)
    return s


def new_image(img):
    return pygame.image.load(assets_path(img)).convert()


def flatten(arr):
    rt = []
    for i in arr:
        if isinstance(i, list): rt.extend(flatten(i))
        else: rt.append(i)
    return rt


textures = {
    "fallback": pygame.image.load(assets_path("fwb:fallback")),
    "version_text": font.render((game_name + " " + game_version_display), False, "white")
}
