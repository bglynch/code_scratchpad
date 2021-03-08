# Sets

https://docs.python.org/3/tutorial/datastructures.html?#sets

https://docs.python.org/3/library/stdtypes.html#set



#### Set construction

```python
# create set
l = {'spam', 'eggs'}        # literal syntax, faster than constructor
l = set(['spam', 'eggs'])   # constructor

# create set from list
l = ['spam', 'eggs', 'spam']
set(l)
>>> {'eggs', 'spam'}

list(set(l))
>>> ['eggs', 'spam']
```



#### Set Modification

```python
s = {'red', 'green', 'blue'}

s.add('yellow')                               
>>> {'blue', 'green', 'red', 'yellow'}

# remove() method raises KeyError if item not in set, discard does nothing
s.remove('black')    
s.discard('orange')
>>>{'blue', 'green', 'red', 'yellow'}

# removes random item from a set and returns it
s.pop()    

# empty the set
s.clear()  
```



#### Query set

```python
s = {'red', 'green', 'blue'}

'red' in s
>>> True
```



#### Set Operations

#### ![Python-Set-Operatioons](images/Python-Set-Operatioons.png)

```python
A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}

# Union
A | B         # operator
A.union(B)    # method
>>> {'blue', 'green', 'orange', 'red', 'yellow'}

# Intersection
A & B               # operator
A.intersection(B)   # method
>>> {'red'}

# Difference
A - B               # operator
A.difference(B)     # method
>>> {'blue', 'green'}

# Symmetric Difference
A ^ B                       # operator
A.symmetric_difference(B)   # method
>>> {'orange', 'blue', 'green', 'yellow'}

# isdisjoint() => returns True if two sets have no items in common
A.isdisjoint(B)
>>> False
A.isdisjoint({'violet', 'indago'})
>>> True
```



## Inplace Modifying a Set

```python
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}
```

###### Update

```python
x1 |= x2
x1
>>> {'qux', 'foo', 'bar', 'baz'}

x1.update(['corge', 'garply'])
x1
>>> {'qux', 'corge', 'garply', 'foo', 'bar', 'baz'}
```

###### ---

```python
x1 &= x2
x1
>>> {'foo', 'baz'}

x1.intersection_update(['baz', 'qux'])
x1
>>> {'baz'}
```

###### ---

```python
x1 -= x2
x1
>>> {'bar'}

x1.difference_update(['foo', 'bar', 'qux'])
x1
>>> set()
```

###### ---

```python
x1 ^= x2
x1
>>> {'bar', 'qux'}

x1.symmetric_difference_update(['qux', 'corge'])
x1
>>> {'bar', 'corge'}
```



#### Built in functions

```python
set.all()	       # Returns True if all items in a set are true
set.any()	       # Returns True if any item in a set is true
set.enumerate()	 # Takes a set and returns an enumerate object
set.len()	       # Returns the number of items in the set
set.max()	       # Returns the largest item of the set
set.min()	       # Returns the smallest item of the set
set.sorted()	   # Returns a sorted set
set.sum()	       # Sums items of the set
```



#### Set Comprehension

```python
{x for x in 'abracadabra' if x not in 'abc'}
>>> {'r', 'd'}
```

