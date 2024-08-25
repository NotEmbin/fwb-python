import pygame
import other
import tags
import textures
import data
from textures import get_texture
from sys import exit
from better_log import log

pygame.init()
window_width = 1600
window_height = 900
screen = pygame.display.set_mode((window_width, window_height), vsync=False)
pygame.display.set_caption(other.game_name)
clock = pygame.time.Clock()
tick = 0
anim_tick = 0

print = log.new_log # NOQA

test_num = int((2**63) - 1)
print(test_num)


def texture(texture_name):
    return other.textures[texture_name].convert()


def show_character(chara_id, pos):
    chara_text = other.to_namespace(chara_id).replace(":", ":character/")
    frames = data.registry["character"][chara_id]["frames_of_animation"]
    width = 125
    height = 125
    x = pos[0]
    y = pos[1]
    if frames != 1:
        chara_text = (chara_text + "/" + str((anim_tick % frames) + 1))
    if other.to_namespace(chara_id) in tags.tags["character"]["fwb:increased_size"]:
        height = 150
        y -= 15
    if other.to_namespace(chara_id) in tags.tags["character"]["fwb:flipped_texture"]:
        screen.blit(pygame.transform.flip(get_texture(chara_text, width, height), True, False), (x, y))
    else:
        screen.blit(get_texture(chara_text, width, height), (x, y))


print("test warn", "warn")
print("test error", "error")
print("test fatal", "fatal")

should_dump = False
textures.load_textures(dump=should_dump)
data.load_registries(dump=should_dump)
tags.load_tags(dump=should_dump)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("#4f0000")

    # screen.blit(get_texture("misc/selection_1", 80, 40), (200, 400))
    # screen.blit(get_texture("test:white", 80, 40), (200, 450))
    # screen.blit(get_texture("fwb:i_do_not_exist_lololol", 80, 40), (200, 500))
    xxx = 5
    yyy = 5
    for _ in data.registry["character"].keys():
        # show_character(_, (xxx, yyy))
        screen.blit(get_texture(_.replace(":", ":character_icon/"), 70, 70), (xxx, yyy))
        xxx += 75
        if xxx >= 1575:
            xxx = 5
            yyy += 75

    screen.blit(texture("version_text"), (7, 690))

    pygame.display.update()
    clock.tick(60)
    tick += 1
    anim_tick = (tick / 2).__floor__()
