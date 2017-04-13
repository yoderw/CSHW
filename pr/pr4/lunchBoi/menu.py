'''
Use case:
menu = Menu(player.inventory); see vision1.txt for eg.

Maybe try curses.panel for stacking menus?
'''
import curses

class MenuItem:

    def __init__(self):
        pass

class Menu:

    def __init__(self, screen, menuItems):
        self.screen = screen
        self.menuItems = menuItems
        self.current = 0
        self.selected = 0

    def update(self):
        pass

    def display(self):
        screen = self.screen
        for item in self.menuItems:
            screen.addstr(" " + item + "\n")

    def cursorSelect(self):
        pass

    def cursorUp(self):
        if self.selected != 0:
            self.selected -= 1

    def cursorDown(self):
        if self.selected != len(self.items) - 1:
            self.selected += 1
