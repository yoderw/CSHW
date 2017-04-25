'''
Use case:
menu = Menu(player.inventory); see vision1.txt for eg.

Maybe try curses.panel for stacking menus?
'''
import curses
from cursor import Cursor
from header import *
from footer import *
from world import World, Room
from items import Item, Key, Chest

def initWorld():
    global world
    world = World()
    player = world.player

def initCurses():
    global stdscr
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(False)
    stdscr.keypad(True)

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

    def __init__(self, screen, world, key="", menuItems={}, init_y=0, init_x=4):
        self.screen = screen
        self.world = world
        self.player = world.player
        self.menuItems = menuItems
        self.menuItemsls = [i for i in menuItems]
        self.menuItemsls.sort()
        self.depth = len(menuItems)
        self.depthIndex = self.depth - 1

        self.header = Header(self)
        self.footer = Footer(self)

        self.init_y = init_y
        self.y = self.init_y_adjust = self.init_y + self.header.height + self.header.y + self.header.spacer
        self.x = self.init_x = init_x
        self.selected = 0

        self.key = key
        self.linked = {}
        self.keysList = []
        self.keysListOrd = []

        # Init self.cursor
        self.cursor = Cursor(self)
        self.world.menus.append(self)

    def link(self, menu):
        self.linked[menu.key] = menu
        menu.linked[self.key] = self
        self.keysList = [i for i in self.linked]
        #self.keysList.sort()
        self.keysListOrd = [ord(i) for i in self.keysList]

    def updateKeys(self):
        self.keysList = [i for i in self.linked]
        #self.keysList.sort()
        self.keysListOrd = [ord(i) for i in self.keysList]

    def addMenuItem(self, item):
        self.menuItems[item.name] = item.action

    def removeMenuItem(self, item):
        self.menuItems.pop(item.name)

    def refreshMenuItems(self, menuItems=None):
        if menuItems is None:
            menuItems = self.menuItems
        self.menuItems = menuItems

    def updateMenuItems(self, dict={}):
        if not dict:
            self.menuItems = self.menuItems
        else:
            self.menuItems = dict
        self.menuItemsls = [i for i in self.menuItems]
        self.menuItemsls.sort()
        self.depth = len(self.menuItems)
        self.depthIndex = self.depth - 1

    def update_y(self):
        self.y = self.init_y_adjust = self.init_y + self.header.height + self.header.y + self.header.spacer

    #TEMP
    def update(self):
        self.updateMenuItems()
        self.updateKeys()

        self.header.update()
        self.update_y()
        self.footer.update()

        self.cursor.update()
    #END

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
    '''
    #TEMP
    def footerRefresh(self):
        item = self.menuItemsls[self.selected]
        item = self.menuItems[item]
        if type(item) is Item:
            self.footer.updateString(item.desc)
    #END
    '''
    def drawHeader(self, y=0, x=0):
        if self.header:
            self.header.draw(y, x)

    def drawFooter(self, y=0, x=0):
        if self.footer:
            self.footer.draw(y, x)

    def drawCursor(self):
        self.cursor.draw()

    def drawMenuItems(self):
        screen = self.screen
        i = self.init_y_adjust
        for item in self.menuItemsls:
            screen.addstr(i, self.init_x + 2, item + "\n")
            i += 1

    def drawAll(self):
        screen = self.screen
        self.drawHeader()
        self.drawCursor()
        self.drawMenuItems()
        footer_y = self.footer.y + self.init_y_adjust + len(self.menuItemsls)
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
        pass

    def cursorUp(self):
        self.cursor.moveUp()
        if self.selected > 0:
            self.selected -= 1
        else:
            self.selected = self.depthIndex
        '''
        #TEMP
        self.footerRefresh()
        #END
        '''

    def cursorDown(self):
        self.cursor.moveDown()
        if self.selected < self.depthIndex:
            self.selected += 1
        else:
            self.selected = 0
        '''
        #TEMP
        self.footerRefresh()
        #END
        '''

class MapView(Menu):

    def __init__(self, screen, world):
        Menu.__init__(self, screen, world, 'm')
        self.menuItems = self.player.location.neighbors
        self.header = MapHeader(self)
        self.footer = MapFooter(self)

    def cursorSelect(self):
        player = self.player
        screen = self.screen
        selected = self.menuItemsls[self.selected]
        selected = self.menuItems[selected]
        live = True
        while True:
            if live:
                room = selected
                if player.canTravel(room) == True:
                    self.drawStringSolo("You are now in room " + room.name)
                    player.travel(room)
                    self.selected = 0
                else:
                    self.drawStringSolo("The door is locked.")
                self.updateMenuItems(player.location.neighbors)
                live = False
            event = screen.getch()
            if event == curses.KEY_LEFT:
                self.update()
                break

class InvView(Menu):

    def __init__(self, screen, world):
        Menu.__init__(self, screen, world, 'i')
        self.menuItems = self.player.inventory
        self.header = InvHeader(self)
        self.footer = InvFooter(self)

    # Not working???
    def cursorSelect(self):
        player = self.player
        screen = self.screen
        selected = self.menuItemsls[self.selected]
        selected = self.menuItems[selected]
        live = True
        while True:
            #TEMP
            item = selected.desc
            self.drawStringSolo(item)
            self.updateMenuItems(player.inventory)
            #END
            event = screen.getch()
            if event == curses.KEY_LEFT:
                self.update()
                break

class RoomView(Menu):

    def __init__(self, screen, world):
        Menu.__init__(self, screen, world, 'r')
        self.menuItems = self.player.location.items
        self.header = RoomHeader(self)
        self.footer = RoomFooter(self)

    def cursorSelect(self):
        pass

class TitleView(Menu):

    def __init__(self, screen, world):
        Menu.__init__(self, screen, world, 'q')

    def cursorSelect(self):
        pass
