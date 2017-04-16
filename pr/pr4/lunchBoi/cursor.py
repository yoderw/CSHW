import curses

class Cursor:

    def __init__(self, menu, depth, string='>', blink=False):
        self.menu = menu
        self.screen = self.menu.screen
        self.depth = depth
        self.x = self.init_x = self.menu.init_x
        self.y = self.init_y = self.menu.init_y_adjust
        self.min_y = self.init_y
        self.max_y = self.init_y + (self.depth - 1)
        self.string = string
        self.blink = blink

    def draw(self):
        screen = self.screen
        if self.blink:
            screen.addstr(self.y, self.x, self.string, curses.A_BLINK)
        else:
            screen.addstr(self.y, self.x, self.string)

    def moveUp(self)  :
        if self.y > self.min_y:
            self.y -= 1
        else:
            self.y = self.max_y

    def moveDown(self):
        if self.y < self.max_y:
            self.y += 1
        else:
            self.y = self.min_y
