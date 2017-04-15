'''
Use case:
menu = Menu(player.inventory); see vision1.txt for eg.

Maybe try curses.panel for stacking menus?
'''
import curses
from cursor import Cursor

#TEMP
def initCurses():
    global stdscr
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(False)
    stdscr.keypad(True)

def termCurses():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    quit()
#END

class MenuItem:

    def __init__(self):
        pass

class Menu:

    def __init__(self, screen, menuItems, init_y=0, init_x=0):
        self.screen = screen
        self.menuItems = menuItems
        self.menuItemsList = [i for i in menuItems]
        self.menuItemsList.sort()
        self.depth = len(menuItems)
        self.depthIndex = self.depth - 1
        self.init_y = init_y
        self.init_x = init_x
        self.selected = 0
        self.cursor = Cursor(self, self.depth)

    def update(self):
        pass

    def draw(self):
        screen = self.screen
        i = self.init_y
        for item in self.menuItemsList:
            screen.addstr(i, self.init_x + 2, item + "\n")
            i += 1

    def drawString(self, str):
        screen = self.screen
        screen.clear()
        screen.addstr(str)
        screen.refresh

    def cursorSelect(self):
        #TEMP
        screen = self.screen
        item = self.menuItemsList[self.selected]
        item = self.menuItems[item]
        while True:
            self.drawString(item)
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

    def loop(self):
        screen = self.screen
        self.draw()
        self.cursor.draw()
        while True:
            event = screen.getch()
            if event == curses.KEY_RIGHT:
                #curses.KEY_ENTER is not recognized
                self.cursorSelect()
            elif event == curses.KEY_UP:
                self.cursorUp()
            elif event == curses.KEY_DOWN:
                self.cursorDown()
            elif event == ord('q'):
                break
            screen.clear()
            self.cursor.draw()
            self.draw()
            screen.refresh()


#TEMP
initCurses()
menuItems = {"Item1":"Action1",
             "Item2":"Action2",
             "Item3":"Action3",
             "Item4":"Action4"
             }
menu = Menu(stdscr, menuItems)
curses.wrapper(Menu.loop(menu))
termCurses()
quit()
#END

#NOTES
#can exec code in values using exec(value)
menuItems = {
"Item1":'''
screen.clear()
stdscr.addstr("Item1 Action")
screen.refresh
''',
"Item2":'''
screen.clear()
stdscr.addstr("Item2 Action")
screen.refresh
''',
"Item3":'''
screen.clear()
stdscr.addstr("Item3 Action")
screen.refresh
''',
"Item4":'''
screen.clear()
stdscr.addstr("Item4 Action")
screen.refresh
'''
            }
#END
