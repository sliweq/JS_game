# from abc import ABC, abstractmethod
from dataclasses import dataclass

import pygame
from pygame import Surface
from pygame.font import Font



@dataclass
class Text:
    text: str
    font: Font
    color: tuple[int, int, int]


class Button:
    def __init__(
        self,
        pos: tuple[int, int],
        size: tuple[int, int],
        text: Text,
        color: tuple[int, int, int] = None,
        color2: tuple[int, int, int] = None,
        image: Surface = None,
    ) -> None:
        self.image = image
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.color = color
        self.color2 = color2
        if text:
            self.text = text.font.render(text.text, 1, text.color)

    def update(self, surface: Surface, mouse_pos: tuple[int, int]) -> bool:
        if self.image:
            surface.blit(self.image, (self.x, self.y))

        pygame.draw.rect(
            surface,
            self.color if self.check_position(mouse_pos) else self.color2,
            (self.x, self.y, self.width, self.height),
        )
        surface.blit(self.text, (self.x, self.y))

    def check_position(self, mouse_pos: tuple[int, int]) -> bool:
        if self.x < mouse_pos[0] < self.x + self.width:
            if self.y < mouse_pos[1] < self.y + self.height:

                return True
        return False
