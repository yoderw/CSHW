class Node:

	def __init__(self, value, next=None):
		self.value = value
		self.next = next

class Queue:

	def __init__(self):
		self.first = None
		self.last = None

	def enqueue(self, value):
		if self.first:
			tail = Node(value)
			self.last.next = tail
			self.last = tail
		else:
			self.first = Node(value)
			self.last = self.first

	def dequeue(self):
		head = self.first
		if self.first is self.last:
			self.first = self.last = None
		else:
			self.first = self.first.next
		return head.value if head else None

	def head(self):
		return self.first.value if self.first else None
