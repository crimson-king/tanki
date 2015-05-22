__author__ = 'Tomasz Rzepka'

import pygame, sys

class Game:
    def __init__(self, manager, width=860, height=600):
        self.manager = manager
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.fps = 60  # #pcmasterrace
        self.clock = pygame.time.Clock()

    def start(self):
        while self.manager.running():
            time = self.clock.tick(self.fps)
            self.run(time)
        pygame.quit()

    def run(self, time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            self.manager.input(event)
        self.manager.update(time)
        self.manager.display(self.screen)
        pygame.display.flip()

