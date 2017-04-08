import os, curses
from curses import wrapper
from character import Character, Player
from world import Room, World
from item import Item, Key

# curses initialization
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

# this will house the main game-loop... I think
def main(stdscr):
    # Clear screen
    stdscr.clear()

    stdscr.refresh()
    stdscr.getkey()
wrapper(main)

# curses termination
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
