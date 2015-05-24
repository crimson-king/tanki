__author__ = 'Tomasz Rzepka'
import pygame
from pygame.sprite import Sprite

TANKS = ['Assets/tank1.png', 'Assets/tank2.png', 'Assets/tank3.png', 'Assets/tank4.png']

class Tank(Sprite):
    def __init__(self, tank_id):
        super(Tank, self).__init__()
        self.tank_id = tank_id
        #self.sprite = pygame.Surface((50, 50))
        self.image = pygame.image.load(TANKS[tank_id % 4])
        self.rect = self.image.get_rect()

    def change_image(self, tank_id):
        self.tank_id = tank_id % 4
        self.image = pygame.image.load(TANKS[tank_id % 4])

class Bullet(Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.sprite = pygame.Surface((10, 10))
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

class Wall(Sprite):
    def __init__(self, loc_x, loc_y):
        super(Wall, self).__init__()
        self.loc = (loc_x, loc_y)
        self.sprite = pygame.Surface((10, 10))
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 100, 0))
        self.rect = self.image.get_rect()
