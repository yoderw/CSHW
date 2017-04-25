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
from menu import MapView, InvView, RoomView, TitleView
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
foo = Item("foo", "bar")
player.invAddItem(B3.key)
player.invAddItem(foo)

mapView = MapView(stdscr, world)
invView = InvView(stdscr, world)
#roomView = RoomView(stdscr, world)
#titleView = TitleView(stdscr, world)
mapView.link(invView)
world.update()

wrapper(loop(mapView))
termCurses()
#quit()
### END ###
