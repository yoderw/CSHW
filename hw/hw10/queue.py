"""
---------------------
Enqueue of 1.
You modified that queue correctly.
---------------------
Enqueue of 2.
You modified that queue correctly.
---------------------
Enqueue of 3.
You modified that queue correctly.
---------------------
Dequeue of 1.
You modified that queue correctly.
---------------------
Enqueue of 4.
You modified that queue correctly.
---------------------
Dequeue of 2.
You modified that queue correctly.
---------------------
Dequeue of 3.
You modified that queue correctly.
---------------------
Dequeue of 4.
Your queue appears empty but 'last' is not None.
You must have modified that queue incorrectly.
---------------------
A test of 'Queue' did not pass.
"""
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
		self.first = self.first.next
		return head.value

	def head(self):
		return self.first.value
