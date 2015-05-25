__author__ = 'Tomasz Rzepka'

import pygame
import sys


class Game:
    def __init__(self, screen, game_data, bg_color=(0, 0, 0)):
        self.screen = screen
        self.bg_color = bg_color
        self.game_data = game_data
        self.clock = pygame.time.Clock()
        self.mouse_is_visible = False
        self.mainloop = False

    def stop(self):
        self.screen.fill((0, 0, 0))
        self.game_data.clear()
        self.mainloop = False

    def mouse_visibility(self):
        if self.mouse_is_visible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)

    def run(self):
        self.mainloop = True
        while self.mainloop:
            self.screen.fill((0, 0, 0))
            self.clock.tick(100)
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.interpret_key(event.key)

            self.mouse_visibility()
            self.game_data.sprites.draw(self.screen)
            pygame.display.flip()

    def interpret_key(self, key):  # hardcoded for debug purposes
        if key == pygame.K_UP:
            self.game_data.players[0].tank.forward()
        elif key == pygame.K_DOWN:
            self.game_data.players[0].tank.backward()
        elif key == pygame.K_LEFT:
            self.game_data.players[0].tank.rotate(+10)
        elif key == pygame.K_RIGHT:
            self.game_data.players[0].tank.rotate(-1)
        elif key == pygame.K_SPACE:
            pass
        elif key == pygame.K_ESCAPE:
            self.stop()
