import curses

def resume():
    # load from save file and run main()
    pass

def save():
    # save progress to file
    pass

def credits():
    # display credits
    pass

def titleScreen(screen):
    while True:
        screen.clear()
        screen.addstr("")
        screen.addstr(' Resume\n')
        screen.addstr(' Save\n')
        screen.addstr(' Credits\n')
        screen.addstr(' Quit\n')
        event = screen.getch()
        if event = curses.KEY_ENTER:
            pass
        elif event = curses.KEY_UP:
            pass
        elif event = curses.KEY_DOWN:
            pass
