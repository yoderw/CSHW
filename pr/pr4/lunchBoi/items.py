class Item:

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.perishable = False
        self.action = None

class Key(Item):

    def __init__(self, name, descr, door):
        Item.__init__(self, name, descr)
        self.door = door

class Chest(Item):

    def __init__(self):
        pass
