'''
To Do:
-- impliment fromRoom/toRoom in items.Key
-- add Room.size and toRoom direction
-- menu classes
-- menu population
-- curses
    -- cursor
    -- menu draw
'''
import os, curses
from curses import wrapper
from player import Player
from world import Room, World
from items import Item, Key
from menu import Menu

### FOR TESTING ###
world = World()
player = world.player
world.newRoom('B1')
world.newRoom('B3')
world.newRoom('B2', ['B1', 'B3'])
world.setStart('B1')
B3 = world.rooms['B3']
B3Key = Key("B3 Key", "This opens room B3.", B3)
B3.key = B3Key
B3.lock()
player.inventory = ["Item1", "Item2", "Item3"]
### END ###

def initCurses():
    global stdscr
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

def termCurses():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

# below is a work in progress
def main(stdscr):
    # Clear stdscr
    stdscr.clear()

    while True:
        event = stdscr.getch()
        if event == curses.KEY_ENTER:
            stdscr.clear()
            stdscr.addstr("KEY_ENTER\n")
            '''
            menu.cursorSelect()
            '''
        elif event == curses.KEY_UP:
            stdscr.clear()
            stdscr.addstr("KEY_UP")
            '''
            menu.cursorUp()
            '''
        elif event == curses.KEY_DOWN:
            stdscr.clear()
            stdscr.addstr("KEY_DOWN")
            '''
            menu.cursorDown()
            '''
        elif event == ord('c'):
            # Character Sheet
            stdscr.clear()
            stdscr.addstr("Character Sheet\n")
            menuItems = player.inventory
            menu = Menu(stdscr, menuItems)
        elif event == ord('r'):
            # Room View
            stdscr.clear()
            stdscr.addstr("Room View\n")
            '''
            menuItems = player.location.items
            menu = Menu(stdscr, menuItems)
            '''
        elif event == ord('m'):
            # Map View
            stdscr.clear()
            stdscr.addstr("Map View")
            '''
            menuItems = player.location.neighbors
            menu = Menu(stdscr, menuItems)
            '''
        elif event == ord('q'):
            # Title stdscr
            break
        menu.display()
        stdscr.refresh()
        #stdscr.getkey()

initCurses()
wrapper(main)
termCurses()
