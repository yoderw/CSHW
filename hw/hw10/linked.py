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
		for i in range(index):
			curr = curr.next
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
			for i in range(1, index):
				curr = curr.next
			curr.next = Node(value, curr.next)

	def delete(self, index):
		if index == 0:
			self.start = self.start.next
		else:
			prior = self.start
			curr = prior.next
			for i in range(1, index):
				prior = curr
				curr = curr.next
			prior.next = curr.next

	def sum(self):
		if self.start is None:
			return 0
		else:
			sum = 0
			curr = self.start
			while curr:
				sum += curr.value
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
		i = 0
		curr = self.start
		while curr:
			if curr.value == value:
				self.delete(i)
			else:
				i += 1
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

class DNode:

	def __init__(self, value, prev=None, next=None):
		self.value = value
		self.next = next
		self.prev = prev

class DLinked(Linked):

	def __init__(self):
		self.start = None
		self.end = None

	def append(self, value):
		if self.start is None:
			self.start = DNode(value)
			self.end = self.start
		elif self.start is self.end:
			self.end = DNode(value, self.start)
			self.start.next = self.end
		else:
			node = DNode(value, self.end)
			self.end.next = node
			self.end = node

	def insert(self, index, value):
		if index == 0:
			if self.start is None:
				self.start = DNode(value)
				self.end = self.start
			else:
				self.start = DNode(value, None, self.start)

		elif index == self.length():
			self.append(value)

		else:
			curr = self.start
			for i in range(1, index):
				curr = curr.next
			if curr.next:
				curr.next = DNode(value, curr, curr.next)
			else:
				curr.next = DNode(value, curr)

	def delete(self, index):
		if index == 0:
			self.start = self.start.next
		else:
			prior = self.start
			curr = prior.next
			for i in range(1, index):
				prior = curr
				curr = curr.next
			prior.next = curr.next
			prior.next.prev = prior
