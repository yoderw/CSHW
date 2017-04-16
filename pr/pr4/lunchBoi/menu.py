'''
Use case:
menu = Menu(player.inventory); see vision1.txt for eg.

Maybe try curses.panel for stacking menus?
'''
import curses
from cursor import Cursor
from header import Header
from footer import Footer

class MenuItem:
    # constructs a menu item from an arbitrary object; eg. a Room or item
    def __init__(self, name, description, action=None):
        self.name = name
        self.description = description
        self.action = action

class Menu:
    # Constructs an interactive menu. Takes a stdscr, a dictionary of menuItems,
    # a header (complex, non-interactive string, placed above interative portion),
    # a footer (complex, non-interactive string, placed below interactive portion),
    # and a init_y/init_x combo. The (y,x) combo dictates the up-left corner.
    # This is the main object used in interacting with the game.
    def __init__(self, screen, menuItems={}, key="", linked={}, header=None, footer=None, init_y=0, init_x=0):
        self.screen = screen
        self.menuItems = menuItems
        self.menuItemsList = [i for i in menuItems]
        self.menuItemsList.sort()
        self.depth = len(menuItems)
        self.depthIndex = self.depth - 1

        # Init self.header
        if header:
            header.menu = self
            self.header = header
        else:
            self.header = Header(self)

        # Init self.footer
        if footer:
            footer.menu = self
            self.footer = footer
        else:
            self.footer = Footer(self)

        self.init_y = init_y
        self.y = self.init_y_adjust = self.init_y + self.header.height + self.header.y + self.header.spacer
        self.x = self.init_x = init_x
        self.selected = 0

        self.key = key
        self.linked = linked
        self.keysList = [i for i in self.linked]
        #self.keysList.sort()
        self.keysListOrd = [ord(i) for i in self.keysList]

        # Init self.cursor
        self.cursor = Cursor(self)

    def update(self):
        self.menuItemsList = [i for i in self.menuItems]
        self.menuItemsList.sort()
        self.depth = len(self.menuItems)
        self.depthIndex = self.depth - 1

        self.y = self.init_y_adjust = self.init_y + self.header.height + self.header.y + self.header.spacer
        self.header.update()
        self.footer.update()

        self.keysList = [i for i in self.linked]
        #self.keysList.sort()
        self.keysListOrd = [ord(i) for i in self.keysList]

        self.cursor = Cursor(self)

    def link(self, menu):
        self.linked[menu.key] = menu
        menu.linked[self.key] = self
        self.update()
        menu.update()

    def menuItemsCompile(self):
        pass

    def headerCompile(self, header):
        if type(header) is str:
            self.header = Header(self, str)
        else:
            header.menu = self
            self.header = header

    def footerCompile(self, footer):
        if type(footer) is str:
            self.footer = Footer(self, str)
        else:
            footer.menu = self
            self.footer = footer

    def linkedCompile(self, keys, menus):
        zipper = zip(keys, menus)
        linked = {i[0]:i[1] for i in zipper}
        self.linked = linked
        for key in linked:
            self.linked[key].linked[self.key] = self
        self.keysList = [i for i in self.linked]

    def drawHeader(self, y=0, x=0):
        if self.header:
            self.header.draw(y, x)

    def drawFooter(self, y=0, x=0):
        if self.footer:
            self.footer.draw(y, x)

    def drawCursor(self):
        self.cursor.draw()

    def drawAll(self):
        screen = self.screen
        self.drawHeader()
        # Draw menu items
        i = self.init_y_adjust
        for item in self.menuItemsList:
            screen.addstr(i, self.init_x + 2, item + "\n")
            i += 1
        # End
        self.drawCursor()
        footer_y = self.footer.y + i
        self.drawFooter(footer_y)

    #TEMP
    def drawStringSolo(self, string, y=0, x=0):
        if y == 0:
            y = self.init_y
        if x == 0:
            x = self.init_x
        screen = self.screen
        screen.clear()
        screen.addstr(y, x, string)
        screen.refresh
    #END

    def cursorSelect(self):
        #TEMP
        screen = self.screen
        item = self.menuItemsList[self.selected]
        item = self.menuItems[item]
        while True:
            self.drawStringSolo(item)
            event = screen.getch()
            if event == curses.KEY_LEFT:
                break
        #END

    def cursorUp(self):
        self.cursor.moveUp()
        if self.selected > 0:
            self.selected -= 1
        else:
            self.selected = self.depthIndex

    def cursorDown(self):
        self.cursor.moveDown()
        if self.selected < self.depthIndex:
            self.selected += 1
        else:
            self.selected = 0
