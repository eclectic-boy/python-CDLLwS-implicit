#python-CDLLwS-implicit

Python implementation of a *Circular Doubly Linked List with Sentinel*. In this version an implicit approach is used namely the `Node` class is hidden within the `CDLLwS` class hence the usage is much more
similar to a normal list.

---

##`CDLLwS` class
The *Doubly Linked List with Sentinel* class itself.
The defined properties/methods are the followings:

###`__init__(self)`

###`__len__(self)`
	
Returns the length of the list (omitting the sentinel object).
```python
l = CDDlwS()
length = len(l)
```

###`__iter__(self)`
	
Transforms this object into an iterator. For example you can do:
```python
l = CDDlwS()
for x in l:
	pass
```

###`__getitem__(self)`

Allows you to positionally retrieve a node, e.g.:
```python
l = CDDlwS()
item = l[27]
```

###`__str__(self)`

Lets you print the `CDLLwS` instance like a normal `list`, e.g.:
```python
l = CDDlwS()
print l
```

###`insert(self, i, data)`

Lets you insert any value (`data`) to any position `i` (*&lt;int&gt;*) of the `CDLLwS` instance like a normal `list`, e.g.:
```python
l = CDDlwS()
l.insert(27, "some text")
```
	
###`append(self, data)`

Lets you append any value (`data`) to the `CDLLwS` instance like a normal `list`, e.g.:
```python
l = CDDlwS()
l.append("some text")
```

###`pop(self, i=-1)`

Lets you remove an element from the `CDLLwS` instance and return it like a normal `list`. If parameter `i` (*&lt;int&gt;*) is equal to `-1` the last item is removed otherwise `i` must be and integer number indicating the position of the item to remove. e.g.:

```python
l = CDDlwS()
x = l.pop(i=27)
```
	
###`index(self, data)`

Returns the index of the first occurrence of `data` in the `CDLLwS` instance. Raises `ValueError` if not present.
```python
l = CDDlwS()
i = l.index("some text")
```
	
###`reverse(self)`

Reverses the order of the`CDLLwS` instance in place.
```python
l = CDDlwS()
l.reverse()
```

---

##Changelog

###1.0.0

First version