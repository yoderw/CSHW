is_even = lambda n: True if n % 2 == 0 else False

def conditional_print(f):
	def printer(n):
		if f(n):
			print(n)
	return printer

print_evens = conditional_print(is_even)