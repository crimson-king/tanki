__author__ = 'Tomasz Rzepka'
import pygame
from pygame.sprite import Sprite


class Tank(Sprite):
    def __init__(self):
        Sprite.__init__()
        self.sprite = pygame.Surface((50, 50))
        self.image.fill((255, 255, 0), 10)
        self.rect = self.image.get_rect()


class Bullet(Sprite):
    def __init__(self):
        Sprite.__init__()
        self.sprite = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0), 10)
        self.rect = self.image.get_rect()