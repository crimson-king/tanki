__author__ = 'Mateusz Jugowiec'

from state import State
import pygame

class GameState(State):
    def __init__(self, bg_color=(0, 0, 0)):

        #self.screen = screen
        self.bg_color = bg_color
        pygame.init()
        self.img = pygame.image.load('tanks2.jpg') # nie wiem czemu u mnie sie z assets nie laduje, wiec zmiencie to :P

    def input(self, event):
        pass

    def display(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.img, (0, 0))
        pygame.display.flip()

    def update(self, event):
        pass

if __name__ == '__main__':
    from state import StateSupervisor, state_manager
    from game_core.game import Game

    state_manager.push(GameState())

    Game(StateSupervisor()).start()