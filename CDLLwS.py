"""
Python implementation of a Circular Doubly Linked List With Sentinel.
In this version the Node class is hidden hence the usage is much more
similar to a normal list.
"""
		
class CDLLwS(object):

	class Node(object):
		def __init__(self, data):
			self.data = data
			self.prev = None
			self.next = None

		def __str__(self):
			return str(self.data)

	def __init__(self):
		self.sentinel = self.Node(None)
		self.sentinel.next = self.sentinel.prev = self.sentinel

		self.len = 0

	def __len__(self):
		return self.len

	def __iter__(self, getNode=False):
		x = self.sentinel.next
		while x != self.sentinel:
			yield x if getNode else x.data
			x = x.next

	def __getitem__(self, i, getNode=False):
		if not -1 <= i < len(self):
			raise IndexError()
		elif i == 0:
			out = self.sentinel.next
		elif i == -1:
			if len(self) > 0:
				out = self.sentinel.prev
			else:
				raise IndexError()
		else:
			for j, x in enumerate(self.__iter__(getNode=True)):
				if j == i:
					out = x
					break
		return out if getNode else out.data

	def _insert_data(self, data, nextNode):
		node = self.Node(data)
		node.prev = nextNode.prev
		node.next = nextNode
		node.prev.next = node
		node.next.prev = node
		self.len += 1

	def insert(self, i, data):
		self._insert_data(
			data,
			self.__getitem__(i, getNode=True) if \
				len(self) > 0 else self.sentinel
		)

	def append(self, data):
		self._insert_data(
			data,
			self.sentinel
		)

	def pop(self, i=-1):
		x = self.__getitem__(i, getNode=True)

		x.prev.next = x.next
		x.next.prev = x.prev
		
		self.len -= 1
		return x.data

	def index(self, data):
		for i, x in enumerate(self):
			if x == data:
				return i
		raise ValueError("'%s' is not in list" % data)

	def reverse(self):
		x = self.sentinel.next
		while x != self.sentinel:
			x.next, x.prev = x.prev, x.next
			x = x.prev
		self.sentinel.next, self.sentinel.prev = self.sentinel.prev, self.sentinel.next

	def __str__(self):
		return str(list(self))

	def __repr__(self):
		return str(self)