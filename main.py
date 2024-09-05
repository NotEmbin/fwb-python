import pygame
import other
import data
import tags
import logging
from menu import Button
from menu import SmallButton
from load import load_resources
from textures import get_texture
from sys import exit

logging.basicConfig(format="[%(asctime)s] [%(levelname)s] %(message)s", level=logging.DEBUG)
pygame.init()
window_width = 1280
window_height = 720
screen = pygame.display.set_mode((window_width, window_height), vsync=False)
pygame.display.set_caption(other.game_name)
clock = pygame.time.Clock()
tick = 0
anim_tick = 0

test_num = int((2**63) - 1)
logging.debug(test_num)


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
    if other.to_namespace(chara_id) in tags.get_tag("character", "fwb:increased_size"):
        height = 150
        y -= 15
    if other.to_namespace(chara_id) in tags.get_tag("character", "fwb:flipped_texture"):
        screen.blit(pygame.transform.flip(get_texture(chara_text, width, height), True, False), (x, y))
    else:
        screen.blit(get_texture(chara_text, width, height), (x, y))


load_resources()

test_button: Button = Button(text="Super Duper Text")
test_button_2: Button = Button(text="Super Duper Text Two!")

while True:
    clicked: bool = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked: bool = True

    screen.fill("#4f0000")

    # screen.blit(get_texture("misc/selection_1", 80, 40), (200, 400))
    # screen.blit(get_texture("test:white", 80, 40), (200, 450))
    # screen.blit(get_texture("fwb:i_do_not_exist_lololol", 80, 40), (200, 500))
    xxx = 15
    yyy = 15
    for _ in data.registry["character"].keys():
        # show_character(_, (xxx, yyy))
        screen.blit(get_texture(_.replace(":", ":character_icon/"), 70, 70), (xxx, yyy))
        xxx += 80
        if xxx >= 800:
            xxx = 15
            yyy += 80

    screen.blit(texture("version_text"), (7, 690))
    test_button.render(screen, (1100, 680), clicked)
    test_button_2.render(screen, (640, 100), clicked)
    test_button.render(screen, (640, 600), clicked)

    pygame.display.update()
    clock.tick(60)
    tick += 1
    anim_tick = (tick / 2).__floor__()
