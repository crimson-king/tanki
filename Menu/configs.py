__author__ = 'Tomasz Rzepka'

import pygame

class PlayerKeyBindings:
    def __init__(self,
                 up=pygame.K_UP, down=pygame.K_DOWN, left=pygame.K_LEFT, right=pygame.K_RIGHT, action=pygame.K_SPACE,):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.action = action
