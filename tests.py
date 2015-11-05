import unittest
from CDLLwS import CDLLwS

class Tests(unittest.TestCase):

	def test_append(self):
		l = CDLLwS()
		l.append("a")
		self.assertEqual(list(l), ["a"])
		l.append("b")
		self.assertEqual(list(l), ["a", "b"])
		l.append("c")
		self.assertEqual(list(l), ["a", "b", "c"])
		l.append("d")
		self.assertEqual(list(l), ["a", "b", "c", "d"])
		l.append("e")
		self.assertEqual(list(l), ["a", "b", "c", "d", "e"])
	
	def test_insert(self):
		l = CDLLwS()
		l.insert(0, "a")
		self.assertEqual(list(l), ["a"])
		l.insert(0, "b")
		self.assertEqual(list(l), ["b", "a"])
		l.insert(1, "c")
		self.assertEqual(list(l), ["b", "c", "a"])
		l.insert(2, "d")
		self.assertEqual(list(l), ["b", "c", "d", "a"])
		l.insert(-1, "e")
		self.assertEqual(list(l), ["b", "c", "d", "e", "a"])

	def test_pop(self):
		l = CDLLwS()
		l.append("a")
		l.append("b")
		l.append("c")
		l.append("d")
		l.append("e")
		x = l.pop(2)
		self.assertEqual(x, "c")
		self.assertEqual(list(l), ["a", "b", "d", "e"])
		x = l.pop(0)
		self.assertEqual(list(l), ["b", "d", "e"])
		x = l.pop(-1)
		self.assertEqual(list(l), ["b", "d"])

	def test_index(self):
		l = CDLLwS()
		l.append("a")
		l.append("b")
		l.append("c")
		l.append("d")
		l.append("e")
		self.assertEqual(l.index("a"), 0)
		self.assertEqual(l.index("b"), 1)
		self.assertEqual(l.index("c"), 2)
		self.assertEqual(l.index("d"), 3)
		self.assertEqual(l.index("e"), 4)
		self.assertRaises(ValueError, l.index, "x")

	def test_reverse(self):
		l = CDLLwS()
		l.append("a")
		l.append("b")
		l.append("c")
		l.append("d")
		l.append("e")
		l_ = list(l)
		l.reverse()
		self.assertNotEqual(l_, list(l))
		self.assertEqual(list(l), ["e", "d", "c", "b", "a"])
		l.reverse()
		self.assertEqual(l_, list(l))
		

if __name__ == "__main__":
	unittest.main()