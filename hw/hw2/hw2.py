def feet_to_meters(f):
	return (f / 3) * 0.9144

def is_multiple(a, b):
	return True if a == 0 and b == 0 else b != 0 and a % b == 0

def tens(x):
	return (x % 100) // 10

def reverse(x):
	return ((x % 10) * 100) + (((x % 100) // 10) * 10) + x // 100

def digit(x, n):
	return 0 if (10 ** n) > x else (x % (10 ** (n + 1))) // (10 ** n)

def zap_buzz(n):
	x = [digit(n, i) for i in range(3) if digit(n, i) == 3]
	return (((x and n % 7 == 0) and "zap buzz") or ((n % 7 == 0 and "zap") or (x and "buzz"))) or n

def coins(c):
	q = c // 25
	d = (c % 25) // 10
	n = ((c % 25) % 10) // 5
	p = (((c % 25) % 10) % 5) 
	return q + d + n + p

def cheapest(n):
	trips_a = (n // 11) + 1 if n % 11 else n // 11
	trips_b = (n // 14) + 1 if n % 14 else n // 14
	cost_a = trips_a * 200
	cost_b = trips_b * 250
	return (cost_a <= cost_b and 'Alice') or (cost_b < cost_a and 'Bob')