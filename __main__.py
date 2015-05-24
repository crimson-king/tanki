__author__ = 'Pawel Kalecinski'

import Menu
import pygame
import sys
if __name__ == "__main__":

    def _creator():
        screen2 = pygame.display.set_mode((800, 600), 0, 32)
        gr = Menu.NewGame(screen2)
        gr.run()

    def _credits():
        screen3 = pygame.display.set_mode((800, 600), 0, 32)
        cr = Menu.Credits(screen3)
        cr.run()

    SCREEN = pygame.display.set_mode((800, 600), 0, 32)
    FUNCS = (("New Game", _creator), ("About", _credits), ("Settings", None), ("Exit", sys.exit))
    pygame.display.set_caption("PyTank")
    GM = Menu.GameMenu(SCREEN, FUNCS)
    GM.run()
