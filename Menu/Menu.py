import pygame
import sys

pygame.init()

RED = (255, 0, 0)
ORANGE = (255, 180, 0)


class MenuItem(pygame.font.Font):
    def __init__(self, text, font=None, font_size=30,
                 font_color=RED, (position_x, position_y)=(0, 0)):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.position_x = position_x
        self.position_y = position_y
        self.position = position_x, position_y
        self.is_selected = False

    def set_position(self, x_1, y_1):
        self.position = (x_1, y_1)
        self.position_x = x_1
        self.position_y = y_1

    def set_color(self, color):
        self.font_color = color
        self.label = self.render(self.text, 1, self.font_color)

    def mouse_selection(self, (pos_x, pos_y)):
        if pos_x >= self.position_x and (pos_x <= self.position_x + self.width):
            if pos_y >= self.position_y and \
                    (pos_y <= self.position_y + self.height):
                return True
        return False


class GameMenu():
    def __init__(self, screen, items, funcs, font='armalite.ttf', font_size=100,
                 font_color=RED):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.img = pygame.image.load('tanks.jpg')
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


class GameRun(GameMenu):
    def __init__(self, screen, bg_color=(0, 0, 0)):
        self.screen = screen
        self.bg_color = bg_color
        self.img = pygame.image.load("tanks2.jpg")

    def run(self):
        mainloop = True
        while mainloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    mainloop = False

            self.screen.fill(self.bg_color)
            self.screen.blit(self.img, (0, 0))
            pygame.display.flip()


class Credits():
    def __init__(self, screen, bg_color=(0, 0, 0)):
        self.screen = screen
        self.bg_color = bg_color

    def show_text(self):
        font = pygame.font.Font('armalite.ttf', 60)
        text = font.render("Pawel Kalecinski", 1, (255, 255, 255))
        text2 = font.render("Tomasz Rzepka", 1, (255, 255, 255))
        text3 = font.render("2015", 1, (255, 255, 255))
        self.screen.blit(text, (100, 100))
        self.screen.blit(text2, (100, 200))
        self.screen.blit(text3, (100, 300))

    def run(self):
        mainloop = True
        while mainloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    mainloop = False
            self.screen.fill(self.bg_color)
            self.show_text()
            pygame.display.flip()

if __name__ == "__main__":

    def creator():
        screen2 = pygame.display.set_mode((800, 600), 0, 32)
        gr = GameRun(screen2)
        gr.run()

    def cred_its():
        screen3 = pygame.display.set_mode((800, 600), 0, 32)
        cr = Credits(screen3)
        cr.run()

    MENU_ITEMS = ("New Game", "About", "Exit", "Settings")
    SCREEN = pygame.display.set_mode((800, 600), 0, 32)
    FUNCS = {"New Game": creator, "About": cred_its, "Settings": None, "Exit": sys.exit}
    pygame.display.set_caption("PyTank")
    GM = GameMenu(SCREEN, FUNCS.keys(), FUNCS)
    GM.run()