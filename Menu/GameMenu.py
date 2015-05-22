__author__ = 'Pawel Kalecinski'

from MenuItem import *

class GameMenu:
    def __init__(self, screen, items, funcs, font='Assets/armalite.ttf', font_size=100,
                 font_color=RED, img='Assets/tanks.jpg'):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.img = pygame.image.load(img)
        self.clock = pygame.time.Clock()
        self.funcs = funcs
        self.items = []

        for index, item in enumerate(items):
            menu_item = MenuItem(item, font, font_size, font_color)
            height_text = len(items) * menu_item.height
            position_x = (self.scr_width / 2) - (menu_item.width / 2)
            position_y = (self.scr_height / 2) - (height_text / 2) + \
                         ((index * 2) + index * menu_item.height)
            menu_item.set_position(position_x, position_y)
            self.items.append(menu_item)

        self.mouse_is_visible = True
        self.cur_item = None

    def mouse_visibility(self):
        if self.mouse_is_visible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)

    def item_selection(self, key):
        for item in self.items:
            item.set_italic(False)
            item.set_color(RED)

        if self.cur_item is None:
            self.cur_item = 0
        else:
            if key == pygame.K_UP and \
                    self.cur_item > 0:
                self.cur_item -= 1
            elif key == pygame.K_UP and \
                    self.cur_item == 0:
                self.cur_item = len(self.items) - 1
            elif key == pygame.K_DOWN and \
                    self.cur_item < len(self.items) - 1:
                self.cur_item += 1
            elif key == pygame.K_DOWN and \
                    self.cur_item == len(self.items) - 1:
                self.cur_item = 0

        self.items[self.cur_item].set_italic(True)
        self.items[self.cur_item].set_color(ORANGE)

        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            text = self.items[self.cur_item].text
            self.funcs[text]()

    @staticmethod
    def mouse_select(item, mouse_pos):
        if item.mouse_selection(mouse_pos):
            item.set_color(ORANGE)
            item.set_italic(True)
        else:
            item.set_color(RED)
            item.set_italic(False)

    def run(self):
        mainloop = True
        while mainloop:
            self.clock.tick(100)
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                if event.type == pygame.KEYDOWN:
                    self.mouse_is_visible = False
                    self.item_selection(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.items:
                        if item.mouse_selection(mouse_pos):
                            self.funcs[item.text]()

            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_is_visible = True
                self.cur_item = None

            self.mouse_visibility()
            self.screen.blit(self.img, (0, 0))

            for item in self.items:
                if self.mouse_is_visible:
                    mouse_pos = pygame.mouse.get_pos()
                    self.mouse_select(item, mouse_pos)
                self.screen.blit(item.label, item.position)

            pygame.display.flip()
