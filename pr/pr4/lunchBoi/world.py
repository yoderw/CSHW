class Room:

    # name:= string; eg. "B1"
    # neighbors:= dictionary, representing adjacent rooms; eg. {"B1":<Room Object>}
    # rethink how locked and key function-- maybe only some doors to a room are locked?
    def __init__(self, name, neighbors={}):
        self.name = name
        self.neighbors = neighbors
        self.items = []
        self.occupied = False
        self.locked = False
        self.key = None

    def unlock(self):
        self.locked = False

    def setName(self, name):
        self.name = name

    def addNeighbor(self, room):
        self.neighbors[room.name] = room
        room.neighbors[self.name] = self

    def addItem(self, item):
        self.items.append(item)

    def occupy(self):
        self.occupied = True

class World:

    def __init__(self):
        self.start = None
        self.rooms = {}

    def setStart(self, room):
        self.start = room
        self.rooms[room.name] = room

    def newRoom(self, name, neighbors={}):
        room = Room(name, neighbors)
        for r in room.neighbors:
            self.rooms[r].neighbors[room.name] = room
            room.neighbors[r] = self.rooms[r]
        self.rooms[room.name] = room

    def update(self):
        pass
