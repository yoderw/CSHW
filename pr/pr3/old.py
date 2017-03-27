import random
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
injurycost = 8 #Cost of losing a fight
displaycost = 1 #Cost of displaying between two passive birds
foodbenefit = 2 #Value of the food being fought over
init_hawk = 0
init_dove = 0
init_defensive = 0
init_evolving = 150

########
# Your code here
########

class World:
    def __init__ (self):
        self.birds=[]

    def update(self):
        for bird in self.birds:
            bird.update()

    def free_food(self, n):
        if len(self.birds)>0:
            for i in range(n):
                random.choice(self.birds).eat()

    def conflict(self, n):
        if len(self.birds)>0:
            for i in range(n):
                b1=random.choice(self.birds)
                ls=self.birds.copy()
                ls.remove(b1)
                b2= random.choice(ls)
                b1.encounter(b2)

    def evolvingPlot(self):
        xvals=[]
        yvals=[]
        for bird in self.birds:
            if bird.species=="Evolving Bird":
                xvals.append(bird.weight)
                yvals.append(bird.aggression)
                plot(xvals, yvals)

    def status(self):
        pop={}
        for bird in self.birds:
            if bird.species not in pop:
                pop[bird.species]=1
            else:
                pop[bird.species]+=1
                And=False
                print("There are", end="")
                for species in pop:
                    if And:
                        print(" and" + " " +str(pop[species]) + " " + species + "s", end="")
                    else:
                        print(" " +str(pop[species]) + " " + species + "s", end="")
                        And=True
                        print(" left in this world.")

class Bird:
    def __init__(self, world):
        self.world=world
        world.birds.append(self)
        self.health=100

    def eat(self):
        self.health+=foodbenefit

    def injured(self):
        self.health-=injurycost

    def display(self):
        self.health-=displaycost

    def die(self):
        self.world.birds.remove(self)

    def update(self):
        self.health-=1
        if self.health<=0:
            self.die()

class Dove(Bird):
    species="Dove"

    def update(self):
        Bird.update(self)
        if self.health>=200:
            self.health-=100
            Dove(self.world)

    def defend_choice(self):
        return False

    def encounter(self, bird):
        if bird.defend_choice()==False:
            self.display()
            bird.display()
            random.choice((self, bird)).eat()
        else:
            bird.eat()

class Hawk(Bird):
    species="Hawk"

    def update(self):
        Bird.update(self)
        if self.health>=200:
            self.health-=100
            Hawk(self.world)

    def defend_choice(self):
        return True

    def encounter(self, bird):
        if bird.defend_choice()==False:
            self.eat()
        else:
            winner=random.choice((self, bird))
            if winner==self:
                loser=bird
            else:
                loser=self
            winner.eat()
            loser.injured()

class Defensive(Bird):
    species = "Defensive Bird"

    def update(self):
        Bird.update(self)
        if self.health>=200:
            self.health-=100
            Defensive(self.world)

    def defend_choice(self):
        return True

    def encounter(self, bird):
        Dove.encounter(self, bird)

class Evolving(Bird):
    def __init__ (self, world, aggression=None, weight=None):
        Bird.__init__ (self, world)
        self.species="Evolving Bird"
        if aggression==None and weight==None:
            self.aggression=random.uniform(0,1)
            self.weight=random.uniform(1,3)
        else:
            #print("inherited: ",end="")
            self.aggression=aggression+random.uniform(-0.1,0.1)
            self.weight=weight+random.uniform(-0.05,0.05)
            if self.aggression<=0:
                self.aggression=0
            elif self.aggression>=1:
                self.aggression=1
            if self.weight<=1:
                self.weight=1
            elif self.weight>=3:
                self.weight=3
            #print("a- "+str(self.aggression)+" "+"w- "+str(self.weight))

    def defend_choice(self):
        if random.random()<=self.aggression:
            return True
        else:
            return False

    def encounter(self, bird):
        #print("encountered")
        #print(self, bird)
        x, y=self.defend_choice(), bird.defend_choice()
        if x and y:
            #print("fight")
            if random.random()<=self.weight/(self.weight+bird.weight):
                winner=self
                loser=bird
            else:
                winner=bird
                loser=self
            winner.eat()
            loser.injured()
        elif x and not y:
            #print("self eat")
            self.eat()
        elif not x and y:
            #print("bird eat")
            bird.eat()
        else:
            #print("display")
            self.display()
            bird.display()
            random.choice([self, bird]).eat()

    def update(self):
        if self.health>=200:
            self.health-=100
            Evolving(self.world,self.aggression,self.weight)
        #print(self.weight)
        self.health-=.4+(.6*self.weight)
        if self.health<=0:
            self.die()

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
    w.free_food(10)  #change to 10
    w.conflict(50)  #change to 50
    w.update()
w.status()
w.evolvingPlot()  #This line adds a plot of evolving birds. Uncomment it when needed.
