import pygame
import other
import tags
import textures
import data
from textures import get_texture
from sys import exit
from util import log

pygame.init()
window_width = 1500
window_height = 900
screen = pygame.display.set_mode((window_width, window_height), vsync=False)
pygame.display.set_caption(other.game_name)
clock = pygame.time.Clock()
tick = 0
anim_tick = 0


print = log.new_log # NOQA

test_surface = pygame.Surface((200, 200))
test_surface.fill((248, 0, 248))
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
    if other.to_namespace(chara_id) in data.tall_characters:
        height = 150
        y -= 15
    chara_text = "fwb:misc/selection_4"
    if other.to_namespace(chara_id) in data.characters_with_flipped_texture:
        screen.blit(pygame.transform.flip(get_texture(chara_text, width, height), True, False), (x, y))
    else:
        screen.blit(get_texture(chara_text, width, height), (x, y))


print("test warn", "warn")
print("test error", "error")
print("test fatal", "fatal")

print(data.registry.keys())

should_dump = False
textures.load_textures(dump=should_dump)
data.load_registries(dump=should_dump)
tags.load_tags(dump=should_dump)

print(tags.tags)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("#4f0000")

    screen.blit(get_texture("misc/selection_1", 80, 40), (200, 400))
    screen.blit(get_texture("test:white", 80, 40), (200, 450))
    screen.blit(get_texture("fwb:i_do_not_exist_lololol", 80, 40), (200, 500))
    xxx = 0
    yyy = 0
    for _ in data.registry["character"].keys():
        show_character(_, (xxx, yyy))
        xxx += 125
        if xxx >= 1500:
            xxx = 0
            yyy += 125

    screen.blit(texture("version_text"), (7, 690))

    pygame.display.update()
    clock.tick(60)
    tick += 1
    anim_tick = (tick / 2).__floor__()
