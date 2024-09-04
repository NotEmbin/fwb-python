import pygame
import other
from textures import get_texture

font = other.font
pygame.init()


class ButtonType:
    def __init__(self, texture: str, width: int, height: int):
        self.texture = other.to_namespace(texture)
        self.width = width * 12
        self.height = height * 12

    def get_button_texture(self):
        return get_texture(self.texture, self.width, self.height)


SmallButton: ButtonType = ButtonType("ui/buttons/button_small", 24, 8)
DefaultButton: ButtonType = ButtonType("ui/buttons/button", 48, 8)


class Button:
    def __init__(self, button_type: ButtonType = DefaultButton, text: str = ""):
        self.button_type = button_type
        self.text = font.render(text, False, "white")

    def render(self, screen: pygame.surface.Surface, pos: tuple) -> None:
        screen.blit(self.button_type.get_button_texture(), pos)
        text_width = self.text.get_width()
        text_height = self.text.get_height()
        text_x_offset = (self.button_type.width / 2) - (text_width / 2)
        text_y_offset = (self.button_type.height / 2) - (text_height / 2)
        screen.blit(self.text, (pos[0] + text_x_offset, pos[1] + text_y_offset))
