from math import sqrt

class Car:

	def __init__(self, mpg, fuel_cap, funds):
		self.mpg = mpg
		self.fuel_tank = self.fuel_cap = fuel_cap
		self.funds = funds
		self.x, self.y = 0, 0

	getMoney = lambda self: self.funds
	getLocation = lambda self: [self.x, self.y]
	getGas = lambda self: self.fuel_tank
	getToFill = lambda self: self.fuel_cap - self.fuel_tank
	getDist = lambda self, x, y: sqrt(((self.x - x) ** 2) + ((self.y - y) ** 2))
	getFuelReq = lambda self, dist: dist / self.mpg

	def refill(self):
		self.fuel_tank = self.fuel_cap

	def charge(self, amount):
		self.funds -= amount

	def driveTo(self, x, y):
		dist = self.getDist(x, y)
		fuel_req = self.getFuelReq(dist)
		if fuel_req > self.getGas():
			return False
		else:
			self.x, self.y = x, y
			self.fuel_tank -= fuel_req
			return True

class GasStation:

	def __init__(self, x, y, rate):
		self.x, self.y = x, y
		self.rate = rate

	def refillCar(self, car):
		dist = car.getDist(self.x, self.y)
		price = car.getToFill() * self.rate
		if dist > .001:
			return False
		elif car.getMoney() < price:
			return False
		else:
			car.refill()
			car.charge(price)
			return True

class Taxi(Car):

	def __init__(self, mpg, fuel_cap, funds):
		Car.__init__(self, mpg, fuel_cap, funds)
		self.passenger = False
		self.mile_count = 0

	def driveTo(self, x, y):
		dist = self.getDist(x, y)
		if Car.driveTo(self, x, y):
			if self.passenger:
				self.mile_count += dist
			return True
		else:
			return False

	def pickup(self):
		if self.passenger:
			return False
		else:
			self.passenger = True
			return True

	def dropoff(self):
		if not self.passenger:
			return False
		else:
			self.funds += (2 + (self.mile_count * 3))
			self.mile_count = 0
			self.passenger = False
			return True

class Dispatcher:

	def __init__(self):
		self.fleet = []

	def hire(self, taxi):
		self.fleet.append(taxi)

	def hail(self, x, y):
		candidates = {}
		for taxi in self.fleet:
			dist = taxi.getDist(x, y)
			fuel_req = taxi.getFuelReq(dist)
			if fuel_req < taxi.getGas():
				if not taxi.passenger:
					candidates[dist] = taxi
		if len(candidates) != 0:	
			hailed = candidates.pop(min(candidates))
			hailed.driveTo(x, y)
			hailed.pickup()
			return hailed
			