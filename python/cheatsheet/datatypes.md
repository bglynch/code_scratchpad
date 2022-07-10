# Data Types[¶](https://docs.python.org/3/library/datatypes.html#data-types)

## Dictionary

Python datatype consisting of key/value pairs



#### Basic Intro

Create Dictionary

```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('one', 1), ('two', 2), ('three', 3)])
e = dict({'one': 1, 'two': 2, 'three': 3})
```

Query

```python
student = {'name': 'John', 'age': 25, 'courses': ['Maths', 'Physics']}

student['name']
>>> 'John'
student['height']
>>> """Traceback (most recent call last):
			   ...
			 KeyError: 'height'"""
  
student.get('name')
>>> 'John'
student.get('height')
>>> None
student.get('height', 'not found')
>>> 'not found'
```

Add to dict

```python
student['phone'] = '555-5555-555'
student
>>>{'name': 'John',
 		'age': 25,
    'courses': ['Maths', 'Physics'],
    'phone': '555-5555-555'}
```

Update

```python
student['name'] = 'Jane'
student.update({'age': 26, 'phone': '444-4444-444'})
student
>>> {'name': 'Jane',
     'age': 26,
     'courses': ['Maths', 'Physics'],
     'phone': '444-4444-444'}
```

Delete

```python
del student['age']
student
>>> {'name': 'Jane', 
     'courses': ['Maths', 'Physics'], 
     'phone': '444-4444-444'}
```

Delete but save value

```python
phone = student.pop('phone')
student
>>> {'name': 'Jane', 
     'courses': ['Maths', 'Physics']}
phone
>>> '444-4444-444'
```

In Builts

```python
student = {'name': 'John', 'age': 25, 'courses': ['Maths', 'Physics']}

student.items()
>>> dict_items([('name', 'John'), ('age', 25), ('courses', ['Maths', 'Physics'])])
student.keys()
>>> dict_keys(['name', 'age', 'courses'])
student.values()
>>> dict_values(['John', 25, ['Maths', 'Physics']])
```

Iteration

```python
for key, value in student.items():
	print(key, value)
>>> name John
>>> age 25
>>> courses ['Maths', 'Physics']
```



### Other types of dictionaries

- defaultdict
- OrderedDict
  - maintains keys in insertion order
- UserDict 





## Sets

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

#### ![Python-Set-Operatioons](/Users/br20069521/Desktop/Date-Dump/21-03-07/code_scratchpad/python/general/images/Python-Set-Operatioons.png)

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







## [`collections`](https://docs.python.org/3/library/collections.html#module-collections) — Container datatypes

| type                                                         | description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple) | factory function for creating tuple subclasses with named fields |
| [`deque`](https://docs.python.org/3/library/collections.html#collections.deque) | list-like container with fast appends and pops on either end |
| [`ChainMap`](https://docs.python.org/3/library/collections.html#collections.ChainMap) | dict-like class for creating a single view of multiple mappings |
| [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter) | dict subclass for counting hashable objects                  |
| [`OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict) | dict subclass that remembers the order entries were added    |
| [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict) | dict subclass that calls a factory function to supply missing values |
| [`UserDict`](https://docs.python.org/3/library/collections.html#collections.UserDict) | wrapper around dictionary objects for easier dict subclassing |
| [`UserList`](https://docs.python.org/3/library/collections.html#collections.UserList) | wrapper around list objects for easier list subclassing      |
| [`UserString`](https://docs.python.org/3/library/collections.html#collections.UserString) | wrapper around string objects for easier string subclassing  |



## namedtuple

#### Factory Function for Tuples with Named Fields

- Immutable
- Like a tuple, but has field names and class name
- Useful for creating quick class

Load

```python
from collections import namedtuple
```

Create

```python
City = namedtuple('City', 'name country population coordinates')
City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])
```

Instanciate

```python
cork = City('Cork', 'IE', 202000, (-8.48, 51.9))
cork = City(name='Cork', country='IE', population=202000, coordinates=(-8.48, 51.9))

city_data = ('Cork', 'IE', 202000, (-8.48, 51.9))
cork = City(*city_data)
cork = City._make(city_data)

# namedtuple-ception
LatLong = namedtuple('LatLong', 'lat lng')
dublin = City('Dublin', 'IE', 1400000, LatLong(-6.26, 53.35))
```

Query Object

```python
City._fields
>>> ('name', 'country', 'population', 'coordinates')

cork.name
>>> 'Cork'
cork._asdict()
>>> {'name': 'Cork', 'country': 'IE', 'population': 202000, 'coordinates': (-8.48, 51.9)}

# namedtuple-ception
dublin.name
>>> 'Dublin'
dublin.coordinates.lat
>>> -6.26
```

Modify Object (this is hacky as a namedtuple is made to be **Immutable**)

```python
cork = cork._replace(population = 220000)
```





## SimpleNamespace

##### A simple [`object`](https://docs.python.org/3/library/functions.html#object) subclass that provides attribute access to its namespace, as well as a meaningful repr.

Load

```python
from types import SimpleNamespace
```

Instanciate

```python
city = SimpleNamespace()
city = SimpleNamespace(name='Cork', population=220000)
```

Query Object

```python
city.__dict__
>>> {'name': 'Cork', 'population': 220000}

city.name
>>> 'Cork'

# namedtuple-ception
dublin.name
>>> 'Dublin'
dublin.coordinates.lat
>>> -6.26
```





## dataclasses

This module provides a decorator and functions for automatically adding generated [special method](https://docs.python.org/3/glossary.html#term-special-method)s such as [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__) and [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__) to user-defined classes.

Load

```python
from dataclasses import dataclass, make_dataclass, field
```

Create

```python
@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

InventoryItem = make_dataclass('InventoryItemx',
                   [('name', str),
                     ('unit_price', float),
                    ('quantity_on_hand', int, field(default=0))])

InventoryItem = make_dataclass('InventoryItem',['name', 'unit_price','quantity_on_hand'])
```

Instanciate

```python
item = InventoryItem('cup', 10.2)
item = InventoryItem('cup', 10.2, 5)
```

Query Object

```python
item.__dict__
>>> {'name': 'name', 'unit_price': 10.2, 'quantity_on_hand': 5}
item.__repr__()
>>> "InventoryItem(name='name', unit_price=10.2, quantity_on_hand=5)"

item.name
>>> 'cup'
```



```
git tag -a v1.0 -m ``"$(date +%F)|<INTEGRATION_ACCOUNT>|$(git rev-parse HEAD)"
```
