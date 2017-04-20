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
import curses
from curses import wrapper
from player import Player
from world import Room, World
from items import Item, Key
from menu import Menu
from loop import loop

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

def main(stdscr):
    # Clear stdscr
    stdscr.clear()
    # Insert menu loop

### FOR TESTING ###
initCurses()

world = World()
player = world.player
world.newRoom('B1')
world.newRoom('B3')
world.newRoom('B2', ['B1', 'B3'])
world.setStart('B1')
B3 = world.rooms['B3']
B3.initKey()
player.invAddItem(B3.key)

mapItems = player.location.neighbors
invItems = player.inventory

mapView = Menu(stdscr, world, "Map View", mapItems, 'm')
invView = Menu(stdscr, world, "Inventory", invItems, 'i')
mapView.link(invView)
Menu.updateAll()

wrapper(loop(mapView))
termCurses()
#quit()
### END ###
