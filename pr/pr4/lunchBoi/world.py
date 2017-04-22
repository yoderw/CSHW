from player import Player
from items import Key

class World:

    def __init__(self):
        self.start = None
        self.player = Player(self)
        self.rooms = {}
        self.menus = []

    def setStart(self, r):
        self.start = self.rooms[r]
        self.player.location = self.start
        self.update()

    def newRoom(self, name, neighbors=[]):
        n = neighbors
        room = Room(self, name)
        room.addNeighbors(n)
        self.rooms[room.name] = room

    def updateRooms(self):
        for r in self.rooms:
            self.rooms[r].update()

    def updateMenus(self):
        for menu in self.menus:
            menu.update()

class Room:

    def __init__(self, world, name):
        self.world = world
        self.name = name
        self.neighbors = {}
        self.items = []
        self.occupied = False
        self.locked = False
        self.key = None
        self.discovered = False

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def initKey(self):
        name = self.name + " " + "Key"
        desc = "This key opens room " + self.name
        door = self
        self.key = Key(name, desc, door)
        self.lock

    def addNeighbors(self, neighbors):
        world = self.world
        rooms = world.rooms
        for r in neighbors:
            self.neighbors[r] = rooms[r]
            rooms[r].neighbors[self.name] = self

    def addItem(self, item):
        self.items.append(item)

    def update(self):
        player = self.world.player
        if player.location == self:
            self.occupied = True
            self.discovered = True
        else:
            self.occupied = False
