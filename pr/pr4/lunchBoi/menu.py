import curses

class Menu:

    def __init__(self, items):
        self.items = items
        self.selected = 0

    def cursorUp(self):
        if self.selected != 0:
            self.selected -= 1

    def cursorDown(self):
        if self.selected != len(self.items) - 1:
            self.selected += 1

'''
Use case:
menu = Menu(player.inventory); see vision1.txt for eg.

Maybe try curses.panel for stacking menus?
'''
