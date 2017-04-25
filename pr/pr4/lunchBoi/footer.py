# Footer needs some way to display text dynamically (see vision1.txt)
# I am going to impliment a self.update method that will attempt to help with this
from header import Header

class Footer(Header):
    pass

class MapFooter(Footer):

    def update(self):
        #TEMP
        self.x = 2
        selected = self.menu.menuItemsls[self.menu.selected]
        selected = self.menu.menuItems[selected]
        self.string = '''
  [>] -- Travel to {}
  [I] -- Inventory
  [R] -- Room View
  [Q] -- Quit
        '''.format(selected.name)
        #END
class InvFooter(Footer):

    def update(self):
        selected = self.menu.menuItemsls[self.menu.selected]
        selected = self.menu.menuItems[selected]
        self.string = '''
\"{}\"

  [>] -- Use: {}
  [M] -- Map View
  [R] -- Room View
  [Q] -- Quit
        '''.format(selected.desc, selected.name)

class RoomFooter(Footer):

    def update(self):
        selected = self.menu.menuItemsls[self.menu.selected]
        selected = self.menu.menuItems[selected]
        self.string = '''
  [>] -- Interact: {}
  [I] -- Inventory
  [M] -- Map View
  [Q] -- Quit
        '''.format(selected.name)

class TitleFooter(Footer):
    pass
