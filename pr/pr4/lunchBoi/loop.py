import curses
from menu import Menu
from header import Header
from footer import Footer

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

# menu argument is #TEMP
def loop(menu):
    #menu = titleScreen
    screen = menu.screen
    menu.drawAll()
    while True:
        event = screen.getch()
        #TEMP
        if event == curses.KEY_RIGHT:
            #curses.KEY_ENTER is not recognized???
            menu.cursorSelect()
        #END
        elif event == curses.KEY_UP:
            menu.cursorUp()
        elif event == curses.KEY_DOWN:
            menu.cursorDown()
        elif event == ord('q'):
            break
        #TEMP
        elif event in menu.keysListOrd:
            key = event
            index = menu.keysListOrd.index(key)
            key = menu.keysList[index]
            menu = menu.linked[key]
        #END
        screen.clear()
        #TEMP - menu.update() is quite buggy
        menu.update()
        #END
        menu.drawAll()
        screen.refresh()
