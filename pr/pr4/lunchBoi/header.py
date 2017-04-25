from stringHelpers import heightHelper, widthHelper

class Header:

    def __init__(self, menu, string="", init_y=0, init_x=2, spacer=0):
        self.menu = menu
        self.world = self.menu.world
        self.player = self.world.player
        self.screen = self.menu.screen
        self.string = string
        self.height = heightHelper(self.string)
        self.width = widthHelper(self.string)
        self.y = self.init_y = init_y
        self.x = self.init_x = init_x
        self.spacer = spacer

    def update(self):
        pass

    def draw(self, y=0, x=0):
        if y == 0:
            y = self.y
        if x == 0:
            x = self.x
        if self.string:
            self.screen.addstr(y, x, self.string)

class RoomHeader(Header):

    def update(self):
        location = self.player.location.name
        self.string = "Room " + location
        self.spacer = 2

class MapHeader(Header):

    def update(self):
        location = self.player.location.name
        self.string = "Your Location: " + location
        self.spacer = 1

class InvHeader(Header):

    def update(self):
        self.string = "Inventory"
        self.spacer = 1

class TitleHeader(Header):
    pass
