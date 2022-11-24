import pygame
import random

from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD
from dino_runner.components.game import Game


class Clouds(Game):
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()
        super().__int__(image, self.type)

    def update(self):
        self.x -= Game.game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))