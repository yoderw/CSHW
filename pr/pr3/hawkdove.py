import random
from random import choice, uniform
import tkinter
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
        c.create_text(x,355, anchor='n', text='%s'% (.5*(i+2) ) )
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
<<<<<<< HEAD
injurycost = 1 #Cost of losing a fight
displaycost = 1 #Cost of displaying
foodbenefit = 1 #Value of the food being fought over
=======
injurycost = 10 #Cost of losing a fight
displaycost = 1 #Cost of displaying
foodbenefit = 8 #Value of the food being fought over
>>>>>>> pr3
init_hawk = 0
init_dove = 0
init_defensive = 0
init_evolving = 150

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
        if self.birds:
            for i in range(n):
                    choice(self.birds).eat()

    def conflict(self, n):
        if self.birds:
            for i in range(n):
                bird1 = choice(self.birds)
                omit = self.birds.index(bird1)
                end = len(self.birds) - 1
                bird2 = choice(self.birds[0:omit] + self.birds[omit + 1:end])
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
        length = len(headcount)
        last_mult = True if length > 1 else False
        comma = True if length > 2 else False
        i = 0
        for species in headcount:
            i += 1
            if i == length and last_mult:
                print("and {} {}s ".format(headcount[species], species), end="")
            else:
                if comma:
                    print("{} {}s, ".format(headcount[species], species), end="")
                else:
                    print("{} {}s ".format(headcount[species], species), end="")
        print("alive in this world.")

    def evolvingPlot(self):
        xvals = [] # weight
        yvals = [] # aggr
        for bird in self.birds:
            if bird.species == "Evolving":
                xvals.append(bird.weight)
                yvals.append(bird.aggr)
        plot(xvals, yvals)


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

class Dove(Bird):

    species = "Dove"

    def update(self):
        Bird.update(self)
        if self.health >= 200:
            self.health -= 100
            Dove(self.world)

    def defend_choice(self):
        return False

    def encounter(self, bird):
        if bird.defend_choice():
            bird.eat()
        else:
            self.display()
            bird.display()
            choice([self, bird]).eat()

class Hawk(Bird):

    species = "Hawk"

    def update(self):
        Bird.update(self)
        if self.health >= 200:
            self.health -= 100
            Hawk(self.world)

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

class Defensive(Bird):

    species = "Defensive"

    def update(self):
        Bird.update(self)
        if self.health >= 200:
            self.health -= 100
            Defensive(self.world)

    def defend_choice(self):
        return True

    def encounter(self, bird):
        Dove.encounter(self, bird)

class Evolving(Bird):

    species = "Evolving"

    def __init__(self, world, aggr=None, weight=None):
        Bird.__init__(self, world)
        self.aggr = aggr + uniform(-0.5, 0.5) if aggr else uniform(0,1)
        self.weight = weight + uniform(-0.1, 0.1) if weight else uniform(1,3)
        # self.aggr = aggr + uniform(-0.1, 0.1) if aggr else uniform(0,1)
        # self.weight = weight + uniform(-0.5, 0.5) if weight else uniform(1,3)
        if not 0 <= self.aggr <= 1:
            self.aggr = round(self.aggr)
        if not 1 <= self.weight <= 3:
            self.weight = round(self.weight)

    def update(self):
        if self.health >= 200:
            self.health -= 100
            Evolving(self.world, self.aggr, self.weight)
        self.health -= .4 + (.6 * self.weight)
        if self.health <= 0:
            self.die()

    def defend_choice(self):
        return uniform(0,1) <= self.aggr

    def encounter(self, bird):
        self_def = self.defend_choice()
        bird_def = bird.defend_choice()
        if self_def and bird_def:
            contestants = [self, bird]
            target = self.weight/(self.weight + bird.weight)
            roll = uniform(0,1)
            winner = self if roll <= target else bird
            contestants.remove(winner)
            loser = contestants[0]
            winner.eat()
            loser.injured()
        elif self_def or bird_def:
            self.eat() if self_def else bird.eat()
        else:
            self.display()
            bird.display()
            choice([self, bird]).eat()

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
<<<<<<< HEAD
#w.evolvingPlot()  #This line adds a plot of evolving birds. Uncomment it when needed.
=======
w.evolvingPlot()  #This line adds a plot of evolving birds. Uncomment it when needed.
>>>>>>> pr3
