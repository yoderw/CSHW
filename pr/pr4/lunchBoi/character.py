# PC and NPC characters will inherit from this class,
# though I don't think it will be neccessary in the end
class Character:

    # location:= Room object representing PC's location
    # world:= World object
    def __init__(self, world):
        self.location = None
        self.world = world


class Player(Character):

    # inventory:= list representing Item objects in PC's possession
    def __init__(self, world):
        Character.__init__(self, world)
        self.inventory = []

    # moves PC to specified room only if room is in location.neighbors,
    # the required key is in PC's inventory if locked, or room is not locked
    def travel(self, room):
        if room.name in self.location.neighbors:
            if room.locked:
                if room.key in self.inventory:
                    self.inventory.remove(key)
                    room.unlock()
                    self.location = room
                    room.occupy()
            else:
                self.location = room
                room.occupy()
        self.world.update()
