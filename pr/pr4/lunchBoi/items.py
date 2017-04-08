class Item:

    def __init__(self, name):
        self.name = name

class Key(Item):

    def __init__(self, name, door):
        Item.__init__(self, name)
        self.door = door
