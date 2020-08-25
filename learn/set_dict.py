#Creating an empty set is a bit tricky.
#Empty curly braces {} will make an empty dictionary in Python. To make a set without any elements, we use the set() function without any argument.
a = {}
print(type(a))

a = set()
print(type(a))

#We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.
#We can add a single element using the add() method, and multiple elements using the update() method. The update() method can take tuples, lists, strings or other sets as its argument. In all cases, duplicates are avoided.

#Symmetric Difference of A and B is a set of elements in A and B but not in both (excluding the intersection).
#Symmetric difference is performed using ^ operator. Same can be accomplished using the method symmetric_difference().

a = {1, 2, 3, 4, 5}
print( 1 in a)
b = {4, 5, 6, 7}
print(a | b) # a.union(b)
print(a & b) # a.intersection(b)
print(a - b) # a.difference(b)
print(b - a) # b.difference(a)
print(b ^ a) # b.symmetric_difference(a)

#Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. While tuples are immutable lists, frozensets are immutable sets.
#Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are hashable and can be used as keys to a dictionary.


#While the values can be of any data type and can repeat, keys must be of immutable type (string, number or tuple with immutable elements) and must be unique.
#While indexing is used with other data types to access values, a dictionary uses keys. Keys can be used either inside square brackets [] or with the get() method.
#If we use the square brackets [], KeyError is raised in case a key is not found in the dictionary. On the other hand, the get() method returns None if the key is not found.

#Dictionary comprehension is an elegant and concise way to create a new dictionary from an iterable in Python.
#Dictionary comprehension consists of an expression pair (key: value) followed by a for statement inside curly braces {}.

squares = {x: x*x for x in range(6)}
print(squares)
