__author__ = 'Pawel Kalecinski'

from GameMenu import GameMenu
import pygame

class NewGame(GameMenu):
    def __init__(self, screen, bg_color=(0, 0, 0)):
        self.screen = screen
        self.bg_color = bg_color
        self.img = pygame.image.load("Assets/tanks2.jpg")

    def run(self):
        mainloop = True
        while mainloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    mainloop = False

            self.screen.fill(self.bg_color)
            self.screen.blit(self.img, (0, 0))
            pygame.display.flip()
