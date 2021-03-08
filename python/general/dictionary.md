# Dictionaries

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