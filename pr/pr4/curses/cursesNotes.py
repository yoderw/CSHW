### curses initialization ###
import curses

# returns window object representing the entire screen
stdscr = curses.initscr()

# turns off automatic echoing of keys in terminal window
curses.noecho()

# turns off buffered input mode--
# no longer requires Enter to be pressed for key recognition
curses.cbreak()

# enables recognition and processing of sequences representing keypress events
# (eg. curses.KEY_LEFT)
stdscr.keypad(True)

### wrapper() ###
from curses import wrapper

# initializatizes above methods, and colors if availible
# makes debugging easier by returning the terminal to its original state,
# after wrapper() returns
def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()
wrapper(main)

### curses termination ###
curses.nocbreak()
stdscr.keypad(False)
curses.echo()

# returns terminal to original state
curses.endwin()

### see cursesTest.py for a successful implimentation

### methods and attributes ###

# creates new window; corrdinates are given in (y, x),
# where top-left corner is (0,0)
newwin()

# e.g.
begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)

# use these to obtain values for (y, x), respectively
curses.LINES
curses.COLS

# e.g.: legal coordinates bounded by...
(0,0)
(curses.LINES - 1, curses.COLS - 1)

# updates screen with queued changes
refresh()

# refresh() calls the following two functions...

# updates data structure representing the desired state of screen
noutrefresh()

# updates physical screen to match state recorded in data structure
doupdate()

# e.g.: call to redraw screen before user input
stdscr.refresh()

# pad:= special instance of a window, whose borders can go beyond display
# creation requires pads width/height,
# while refresh requires coordinates of are being displayed
pad = curses.newpad(100, 100)
# These loops fill the pad with letters; addch() is
# explained in the next section
for y in range(0, 99):
    for x in range(0, 99):
        pad.addch(y,x, ord('a') + (x*x+y*y) % 26)

# Displays a section of the pad in the middle of the screen.
# (0,0) : coordinate of upper-left corner of pad area to display.
# (5,5) : coordinate of upper-left corner of window area to be filled
#         with pad content.
# (20, 75) : coordinate of lower-right corner of window area to be
#            filled with pad content.
pad.refresh( 0,0, 5,5, 20,75)

# moves cursor to (y,x)
move(y,x)

# hides cursor
curs_set(False)

# adds a string to stdscrn at current cursos location;
# takes various args, and has various sister functions
# (see docs 4: Displaying Text)
addstr()

# call soon after initscr() to use color;
# called automatically by wrapper()
start_color()

# returns True if colors are enabled on the terminal in use
has_colors()

# obtains the attribute value corresponding to a color pair
color_pair()

# e.g.
stdscr.addstr("Pretty text", curses.color_pair(1))
stdscr.refresh()

# colorpairs consist of a foreground and a background color,
# where 0=black, 1=red, 2=green, 3=yellow, 4=blue, 5=magenta, 6=cyan, 7=white
# and init_pair(n, f, b) assigns color pair n to foreground f and background b
# n=0 is hardwired to f=white, b=black
# curses has defined constants referring to colors:
# e.g.
curses.COLOR_BLACK
curses.COLOR_RED

# e.g.: change n=1 to f=red, b=white
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

# e.g.: display "RED ALERT!" in the UL corner in red
stdscr.addstr(0,0, "RED ALERT!", curses.color_pair(1))
