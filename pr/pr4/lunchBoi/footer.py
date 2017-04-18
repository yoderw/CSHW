# Footer needs some way to display text dynamically (see vision1.txt)
# I am going to impliment a self.update method that will attempt to help with this
from stringHelpers import heightHelper, widthHelper

class Footer:

    def __init__(self, menu, string="", init_y=0, init_x=0, spacer=0):
        self.menu = menu
        self.screen = self.menu.screen
        self.string = string
        self.height = heightHelper(self.string)
        self.width = widthHelper(self.string)
        self.y = self.init_y = init_y
        self.x = self.init_x = init_x
        self.spacer = spacer

    def updateString(self, string=None):
        if string is None:
            string = self.string
        self.string = string

    def update(self):
        pass

    def draw(self, y=0, x=0):
        if y == 0:
            y = self.y
        if x == 0:
            x = self.x
        if self.string:
            self.screen.addstr(y, x, self.string)

class MapFooter(Footer):

    def __init__(self):
        pass

class InvFooter(Footer):

    def __init__(self):
        pass

class RoomFooter(Footer):

    def __init__(self):
        pass
