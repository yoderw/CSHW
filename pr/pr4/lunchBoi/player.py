class Player:

    def __init__(self, world):
        self.world = world
        self.location = None
        self.inventory = {}
        self.discovered = []

    def canTravel(self, r):
        if type(r) is str:
            r = self.world.rooms[r]
        if r.name in self.location.neighbors:
            if r.locked:
                if r.key in self.inventory:
                    return True
                else:
                    return False
            return True
        return False

    def travel(self, r):
        if self.canTravel(r):
            if type(r) is str:
                r = self.world.rooms[r]
            if r.locked:
                #TEMP
                #self.inventory.remove(r.key)
                #END
                r.unlock()
            self.location = r
            self.world.update()

    def invAddItem(self, item):
        self.inventory[item.name] = item
