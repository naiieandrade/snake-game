import pygame

from src.Config import Config


class Snake:
    def __init__(self, display):
        self.x_pos = (Config['game']['width']) / 2
        self.y_pos = (Config['game']['height']) / 2
        self.display = display

    def draw(self):
        return pygame.draw.rect(
            self.display,
            Config['colors']['green'],
            [
                self.x_pos,
                self.y_pos,
                Config['snake']['height'],
                Config['snake']['width']
            ]
        )

    def move(self, x_change, y_change):
        self.x_pos += x_change
        self.y_pos += y_change
