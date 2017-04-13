class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.perishable = False
        #self.activation???

class Key(Item):

    def __init__(self, name, description, door):
        Item.__init__(self, name, description)
        self.door = door

class Chest(Item):

    def __init__(self):
        pass
