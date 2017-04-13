import curses
from curses import wrapper

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

curses.can_change_color()

def main(stdscr):
    # Clear screen
    stdscr.clear()

    while True:
        pass
        
    stdscr.refresh()
    stdscr.getkey()
wrapper(main)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
