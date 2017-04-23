class Item:

    def __init__(self, name, descr):
        self.name = name
        self.descr = descr
        self.perishable = False
        self.action = None

class Key(Item):

    def __init__(self, name, descr, door):
        Item.__init__(self, name, descr)
        self.door = door

class Chest(Item):

    def __init__(self):
        pass
