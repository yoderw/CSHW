"""
notes:
- icost = 7; dcost = 1; fben = 8 should return only hawks.
  instead, I am getting mostly with a handful of doves occasionally.
  look into this probably has to do with conflict
- make defense_choice an attribute and not a method

- The following settings:

    injurycost = 10 #Cost of losing a fight
    displaycost = 1 #Cost of displaying
    foodbenefit = 12 #Value of the food being fought over
    init_hawk = 50
    init_dove = 50
    init_defensive = 50
    init_evolving = 0

    Should as well return only hawks. Instead:

    "There are 37 Defensives and 87 Hawks alive in this world."

    Fix this.

"""


import random
from random import choice
### need to import tkinter module ###
#import tkinter
random.seed()

def plot(xvals, yvals):
    # This is a function for creating a simple scatter plot.  You will use it,
    # but you can ignore the internal workings.
    root = tkinter.Tk()
    c = tkinter.Canvas(root, width=700, height=400, bg='white') #was 350 x 280
    c.grid()
    #create x-axis
    c.create_line(50,350,650,350, width=3)
    for i in range(5):
        x = 50 + (i * 150)
        c.create_text(x,355,anchor='n', text='%s'% (.5*(i+2) ) )
    #y-axis
    c.create_line(50,350,50,50, width=3)
    for i in range(5):
        y = 350 - (i * 75)
        c.create_text(45,y, anchor='e', text='%s'% (.25*i))
    #plot the points
    for i in range(len(xvals)):
        x, y = xvals[i], yvals[i]
        xpixel = int(50 + 300*(x-1))
        ypixel = int(350 - 300*y)
        c.create_oval(xpixel-3,ypixel-3,xpixel+3,ypixel+3, width=1, fill='red')
    root.mainloop()

#Constants: setting these values controls the parameters of your experiment.
injurycost = 10 #Cost of losing a fight
displaycost = 1 #Cost of displaying
foodbenefit = 12 #Value of the food being fought over
init_hawk = 50
init_dove = 50
init_defensive = 50
init_evolving = 0

########
# Your code here
########

class World:

    def __init__(self):
        self.birds = []

    def update(self):
        for bird in self.birds:
            bird.update()

    def free_food(self, n):
        for i in range(n):
            if self.birds:
                choice(self.birds).eat()

    def conflict(self, n):
        birds = self.birds
        if self.birds:
            bird1 = choice(birds)
            omit = birds.index(bird1)
            end = len(birds) - 1
            bird2 = choice(birds[0:omit] + birds[omit + 1:end])
            bird1.encounter(bird2)

    def status(self):
        headcount = {}
        for bird in self.birds:
            species = bird.species
            if species in headcount:
                headcount[species] += 1
            else:
                headcount[species] = 1
        print("There are ", end="")
        if 3 > len(headcount) > 1:
            last_mult = True
            comma = False
        elif len(headcount) > 2:
            last_mult = True
            comma = True
        else:
            comma = False
            last_mult = False
        length = len(headcount)
        i = 0
        for species in headcount:
            i += 1
            if i == length and last_mult:
                print("and {} {}s ".format(headcount[species], species), end="")
            else:
                print("{} {}s ".format(headcount[species], species), end="")
        print("alive in this world.")

class Bird:

    def __init__(self, world):
        self.world = world
        self.health = 100
        self.world.birds.append(self)

    def eat(self):
        self.health += foodbenefit

    def injured(self):
        self.health -= injurycost

    def display(self):
        self.health -= displaycost

    def die(self):
        self.world.birds.remove(self)

    def update(self):
        self.health -= 1
        if self.health <= 0:
            self.die()

class Hawk(Bird):

    species = "Hawk"

    def update(self):
        Bird.update(self)
        if self.health >= 200:
            self.health -= 100
            w = self.world
            w.birds.append(Hawk(w))

    def defend_choice(self):
        return True

    def encounter(self, bird):
        if bird.defend_choice():
            contestants = [self, bird]
            winner = choice(contestants)
            contestants.remove(winner)
            loser = contestants[0]
            winner.eat()
            loser.injured()
        else:
            self.eat()


class Dove(Bird):

    species = "Dove"

    def update(self):
        Bird.update(self)
        if self.health >= 200:
            self.health -= 100
            w = self.world
            w.birds.append(Dove(w))

    def defend_choice(self):
        return False

    def encounter(self, bird):
        if bird.defend_choice():
            bird.eat()
        else:
            self.display()
            bird.display()
            choice((self, bird)).eat()

class Defensive(Bird):

    species = "Defensive"

    def update(self):
        Bird.update(self)
        if self.health >= 200:
            self.health -= 100
            w = self.world
            w.birds.append(Defensive(w))

    def defend_choice(self):
        return True

    def encounter(self, bird):
        Dove.encounter(self, bird)


########
# The code below actually runs the simulation.  You shouldn't have to do anything to it.
########
w = World()
for i in range(init_dove):
    Dove(w)
for i in range(init_hawk):
    Hawk(w)
for i in range(init_defensive):
    Defensive(w)
for i in range(init_evolving):
    Evolving(w)

for t in range(10000):
    w.free_food(10)
    w.conflict(50)
    w.update()
w.status()
#w.evolvingPlot()  #This line adds a plot of evolving birds. Uncomment it when needed.
