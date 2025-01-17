import pygame
import random

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        rand = random.randint(0, 2)
        if len(self.obstacles) == 0:
            if rand == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif rand == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif rand == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break               

    def reset_obstacles(self):
        self.obstacles = []
            
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)