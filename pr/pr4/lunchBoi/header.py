class Header:

    def __init__(self, menu, string="", height=0, width=0, init_y=0, init_x=0, spacer=0):
        self.menu = menu
        self.screen = self.menu.screen
        self.string = string
        self.height = height
        self.width = width
        self.y = self.init_y = init_y
        self.x = self.init_x = init_x
        self.spacer = spacer

    def draw(self, y=0, x=0):
        if y == 0:
            y = self.y
        if x == 0:
            x = self.x
        if self.string:
            self.screen.addstr(y, x, self.string)
