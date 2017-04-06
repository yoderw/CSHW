class Node:

	def __init__(self, value, next=None):
		self.value = value
		self.next = next

class Linked:

	def __init__(self):
		self.first = None

	def display(self):
		print("[", end="")
		if self.first:
			curr = self.first
			while curr.next:
				print(curr.value, end="") 
				print(", ", end="")
				curr = curr.next
			print(curr.value, end="")
		print("]")

	def getValue(self, index):
		curr = self.first
		while index > 0:
			curr = curr.next()
			index -= 1
		return curr.value

	def append(self, value):
		if self.first is None:
			self.first = Node(value)
		else:
			curr = self.first
			while curr.next:
				curr = curr.next
			curr.next = Node(value)

	def isEmpty(self):
		return self.first is None

	def length(self):
		if self.first is None:
			return 0
		else:
			count = 1
			curr = self.first
			while curr.next:
				curr = curr.next
				count += 1
			return count

	def insert(self, index, value):
		if index == 0:
			self.first = Node(value, self.first)
		else:
			curr = self.first
			while index > 1:
				curr = curr.next
				index -= 1
			curr.next = Node(value, curr.next)

	def delete(self, index):
		if index == 0:
			self.first = self.first.next
		else:
			prev = self.first
			curr = prev.next
			while index > 1:
				prev = curr
				curr = curr.next
				index -= 1
			prev.next = curr.next

	def sum(self):
		if self.first is None:
			return 0
		else:
			sum = 0
			curr = self.first
			while curr:
				sum += curr.value
				curr = curr.next
			return sum

	def count(self, value):
		if self.first is None:
			return 0
		else:
			count = 0
			curr = self.first
			while curr:
				count += 1 if curr.value == value else 0
				curr = curr.next
			return count

	def apply(self, func):
		curr = self.first
		while curr:
			curr.value = func(curr.value)
			curr = curr.next

	def deleteAll(self, value):
		i = 0
		curr = self.first
		while curr:
			if curr.value == value:
				self.delete(i)
			else:
				i += 1
			curr = curr.next

class Sorted(Linked):

	def append(self, value):
		if self.first is None:
			self.first = Node(value)
		else:
			if self.first.value > value:
				self.first = Node(value, self.first)
			else:
				prev = self.first
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
		self.first = None
		self.last = None

	def append(self, value):
		if self.first is None:
			self.first = DNode(value)
			self.last = self.first
		elif self.first is self.last:
			self.last = DNode(value, self.first)
			self.first.next = self.last
		else:
			self.last = Node(value, self.last)

	#insert does not work... display appears to remove self.last
	def insert(self, index, value):
		if index == 0:
			self.first = DNode(value, self.first, self.last)
		else:
			curr = self.first
			while index > 1:
				curr = curr.next
				index -= 1
			curr.next = DNode(value, curr, curr.next.next)

	#has not yet been modified
	def delete(self, index):
		if index == 0:
			self.first = self.first.next
		else:
			prev = self.first
			curr = prev.next
			while index > 1:
				prev = curr
				curr = curr.next
				index -= 1
			prev.next = curr.next
