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
        c = stdscr.getch()
        if c == ord('p'):
            print("Success")
        elif c == ord('q'):
            break  # Exit the while()

    stdscr.refresh()
    stdscr.getkey()
wrapper(main)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
