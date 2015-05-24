__author__ = 'Tomasz Rzepka'

from actor import Tank, Wall

class GameData:
    def __init__(self):
        self.players = [Player(i) for i in xrange(4)]
        self.walls = [Wall(i*2+1, 5) for i in xrange(10)]

class Player:
    def __init__(self, tank_id):
        self.isOn = False
        self.tank = Tank(tank_id)

    def turn_on(self):
        self.isOn = True

    def turn_off(self):
        self.tank.change_image(0)
        self.isOn = False
