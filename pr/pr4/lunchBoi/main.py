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
    quit()

def main(stdscr):
    # Clear stdscr
    stdscr.clear()
    # Insert menu loop

initCurses()
wrapper(main)
termCurses()
