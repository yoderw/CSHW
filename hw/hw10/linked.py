class Node:

	def __init__(self, value, next=None):
		self.value = value
		self.next = next

class Linked:

	def __init__(self):
		self.start = None

	def display(self):
		print("[", end="")
		if self.start:
			curr = self.start
			while curr.next:
				print(curr.value, end="") 
				print(", ", end="")
				curr = curr.next
			print(curr.value, end="")
		print("]")

	def getValue(self, index):
		curr = self.start
		while index > 0:
			curr = curr.next()
			index -= 1
		return curr.value

	def append(self, value):
		if self.start is None:
			self.start = Node(value)
		else:
			curr = self.start
			while curr.next:
				curr = curr.next
			curr.next = Node(value)

	def isEmpty(self):
		return self.start is None

	def length(self):
		if self.start is None:
			return 0
		else:
			count = 1
			curr = self.start
			while curr.next:
				curr = curr.next
				count += 1
			return count

	def insert(self, index, value):
	 	if index == 0:
	 		self.start = Node(value, self.start)
	 	else:
	 		curr = self.start
	 		while index > 1:
	 			curr = curr.next
	 			index -= 1
	 		curr.next = Node(value, curr.next)

	def delete(self, index):
	 	if index == 0:
	 		self.start = self.start.next
	 	else:
	 		prev = self.start
	 		curr = prev.next
	 		while index > 1:
	 			prev = curr
	 			curr = curr.next
	 			index -= 1
	 		prev.next = curr.next

	def sum(self):
		if self.start is None:
			return 0
		else:
			sum = 0
			curr = self.start
			while curr:
				count += curr.value
				curr = curr.next
			return sum

	def count(self, value):
		if self.start is None:
			return 0
		else:
			count = 0
			curr = self.start
			while curr:
				count += 1 if curr.value == value else 0
				curr = curr.next
			return count

	def apply(self, func):
		curr = self.start
		while curr:
			curr.value = func(curr.value)
			curr = curr.next

	def deleteAll(self, value):
		prev = self.start
		curr = prev.next
		while curr:
			if curr.value == value:
				prev.next = curr.next
			prev = curr
			curr = curr.next

class Sorted(Linked):

	def append(self, value):
		if self.start is None:
			self.start = Node(value)
		else:
			if self.start.value > value:
				self.start = Node(value, self.start)
			else:
				prev = self.start
				curr = prev.next
				while curr:
					if prev.value <= value <= curr.value:
						break
					prev = curr
					curr = curr.next
				prev.next = Node(value, curr)

