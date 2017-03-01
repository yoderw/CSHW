def brick_maker(s):
	brick = lambda x, y: ((x * s) + '\n') * y
	return brick

def max_of_two(f, g, n):
	return max(f(n), g(n))

def max_of_funcs(f, g):
	h = lambda x: max(f(x), g(x))
	return h