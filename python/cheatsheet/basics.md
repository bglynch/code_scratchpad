# Basics

## Numbers

#### Create

```python
int(2.3)    >>> 2
int(-2.8)   >>> 2
float(5)    >>> 5.0
abs(-10)    >>> 10



'1'.isdigit()    >>> True
'-1'.isdigit()   >>> False
'1.1'.isdigit()  >>> False
```



```python
1905/100   >>> 19.05
1905//100  >>> 19

round(10)        >>> 10
round(10.7)      >>> 11
round(5.5)       >>>  6
round(2.665, 2)  >>> 2.67

import math
math.ceil(1.1)  >>> 2.0
```

## String

```python
str.split(separator, maxsplit)
str.replace(old, new [, count])
txt = "welcome to the jungle"
txt.split()            >>> ['welcome', 'to', 'the', 'jungle']
' '.join(txt.split())  >>> "welcome to the jungle"
```

## List

#### Create

```python
l = ['a', 'b', 'c', 'd']
```

#### Remove item

```python
list.pop(index)  # pop returns the value removed
del list[index]
list.remove(element)  # removes first matching element

l = ['a', 'b', 'c', 'd']
l.pop(0)
>>> 'a'
del l[0]
l
>>> ['c', 'd']

animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']
animals.remove('dog')
>>> ['cat', 'dog', 'guinea pig', 'dog']
```

#### Add Item

```python
list.insert(index, elem)   # adds element to a specified index in a list
list.append(elem)          # adds element to the end of the list

vowel = ['a', 'e', 'i', 'u']
vowel.insert(3, 'o')
>>> ['a', 'e', 'i', 'o', 'u']
```

#### Find Element

```python
list.index(element, start, end)

vowels = ['a', 'e', 'i', 'o', 'i', 'u']
vowels.index('e')
>>> 1
vowels.index('p')
>>> ValueError: 'p' is not in list
```

#### Other

```python
list.count(element)   # returns no. of times the specified element appears in the list
list.reverse()        # inplace reverse of list
list.sort(key=., reverse=.) # inplace sort list in a specific ascending or descending order
   list.sort(reverse=True)

sorted(list, key=., reverse=.) # sort list in a specific ascending or descending order, not inplace
reversed(list)       # reverse list, not inplace
```

#### Slicing

```python
list[start:end:step]

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# get item from the list
my_list[5]        # >>> 5

# get range from a list
my_list[0:6]      # >>> [0, 1, 2, 3, 4, 5]
my_list[1:-7]     # >>> [1, 2]
my_list[-7:-2]    # >>> [3, 4, 5, 6, 7]

# get range from item to start/end of the list
my_list[2:]       # >>> [2, 3, 4, 5, 6, 7, 8, 9]
my_list[:-4]      # >>> [0, 1, 2, 3, 4, 5]

# get range with a step
my_list[2:-1:2]   # >>> [2, 4, 6, 8]

# get range backwards by using a negative step
my_list[-1:2:-1]  # >>> [9, 8, 7, 6, 5, 4, 3]
my_list[::-1]     # >>> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

#### Sorting

```

```

#### Replace certain number

```python
li = [1, 2, 1, 2, 1]

def replace(array, to_replace, replacement):
    return [replacement if x==elemToReplace else x for x in array]


```



## Built Ins

#### checks

```python
string.isalpha()   # returns True if all chars are letters
string.isdecimal() # returns True if all chars in a string are decimal characters
string.isnumeric() # returns True if all chars in a string are numeric characters
```

#### all()

```python
all(iterable)   # returns True if all elements in the given iterable are true
False => 0, False, 
True  => non zero ints, True

all([1, 3, 4, 5])  >>> True  
```







