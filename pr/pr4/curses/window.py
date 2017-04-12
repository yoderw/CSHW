import curses

class Screen:

    def __init__(self, key):
        self.key = key

class Window:

    def __init__(self, rows, cols, screens=[]):
        self.rows = rows
        self.cols = cols
        self.screens = screens

    def screenShift:
        
