import pygame
import other
import logging
from textures import get_texture

font = other.font
small_font = other.font_small
pygame.init()
logging.basicConfig(format="[%(asctime)s] [%(levelname)s] %(message)s", level=logging.DEBUG)


class ButtonType:
    def __init__(self, texture: str, width: int, height: int):
        self.texture = other.to_namespace(texture)
        self.width: int = width * 7
        self.height: int = height * 7

    def get_button_texture(self):
        return get_texture(self.texture, self.width, self.height)

    def get_button_hover_texture(self):
        return get_texture(f'{self.texture}_hover', self.width, self.height)


SmallButton: ButtonType = ButtonType("ui/buttons/button_small", 24, 8)
DefaultButton: ButtonType = ButtonType("ui/buttons/button", 48, 8)


class Button:
    def __init__(self, button_type: ButtonType = DefaultButton, text: str = "", used_font: pygame.font.Font = small_font):
        self.rect = None
        self.clicked: bool = False
        self.font = used_font
        self.button_type = button_type
        self.text = self.font.render(text, False, "white")
        self.text_shadow = self.font.render(text, False, "gray20")
        self.shadow_offset = 2

    def render(self, screen: pygame.surface.Surface, pos: tuple, clicked: bool = False) -> None:
        mx, my = pygame.mouse.get_pos()
        button_x_offset = self.button_type.width / 2
        button_y_offset = self.button_type.height / 2
        self.rect = pygame.Rect(pos[0] - button_x_offset, pos[1] - button_y_offset, self.button_type.width, self.button_type.height)
        if self.rect.collidepoint((mx, my)):
            if clicked:
                print("bleh")
                screen.blit(get_texture("fwb:character_icon/nightmare_freddy", self.button_type.width, self.button_type.height), (pos[0] - button_x_offset, pos[1] - button_y_offset))
            else:
                screen.blit(self.button_type.get_button_hover_texture(), (pos[0] - button_x_offset, pos[1] - button_y_offset))
        else:
            screen.blit(self.button_type.get_button_texture(), (pos[0] - button_x_offset, pos[1] - button_y_offset))
        text_width = self.text.get_width()
        text_height = self.text.get_height()
        text_x_offset = button_x_offset - (self.button_type.width / 2) - (text_width / 2)
        text_y_offset = button_y_offset - (self.button_type.height / 2) - (text_height / 2)
        screen.blit(self.text_shadow, (pos[0] + text_x_offset + self.shadow_offset, pos[1] + text_y_offset + self.shadow_offset))
        screen.blit(self.text, (pos[0] + text_x_offset, pos[1] + text_y_offset))


class Menu:
    def __init__(self):
        pass

    def render(self, screen: pygame.surface.Surface):
        mx, my = pygame.mouse.get_pos()
