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
        if event == curses.KEY_RIGHT:
            #curses.KEY_ENTER is not recognized???
            menu.cursorSelect()
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
        #menu.update()
        #END
        menu.drawAll()
        screen.refresh()

#TEMP
initCurses()

menuItemsA = {"Item1":"Action1",
              "Item2":"Action2",
              "Item3":"Action3",
              "Item4":"Action4"
              }

menuItemsB = {"ItemA":"ActionA",
              "ItemB":"ActionB",
              "ItemC":"ActionC",
              "ItemD":"ActionD"
              }

menuA = Menu(stdscr, menuItemsA, 'a', {}, None, None, 0, 2)
headerA = Header(menuA, "MENU: A", 1, len("MENU: A"), 1, 2)
footerA = Footer(menuA, "FOOTER", 1, len("FOOTER"), 0, 2)
menuA.headerCompile(headerA)
menuA.footerCompile(footerA)

menuB = Menu(stdscr, menuItemsB, 'b', {}, None, None, 0, 2)
headerB = Header(menuB, "MENU: B", 1, len("MENU: B"), 1, 2)
footerB = Footer(menuB, "FOOTER", 1, len("FOOTER"), 0, 2)
menuB.headerCompile(headerB)
menuB.footerCompile(footerB)

menuA.update()
menuB.update()
menuA.link(menuB)

curses.wrapper(loop(menuA))
termCurses()
quit()
#END
