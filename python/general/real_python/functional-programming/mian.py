import collections
from pprint import pprint

# make an Immutable object
Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel'
])

# put them in an Immutable data structure
scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='math', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='physics', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)

# ============================================================================================================= filter()

fs = filter(lambda x: x.nobel is True, scientists)

print(fs)
pprint(tuple(fs))

pprint(tuple(filter(lambda x: x.field == 'physics' and x.nobel, scientists)))


# create reusable filter
def nobel_filter(x):
    return x.nobel is True


pprint(tuple(filter(lambda x: nobel_filter(x), scientists)))

# filtering a list comprehension
print("")
pprint([x for x in scientists if x.nobel is True])
pprint(tuple(x for x in scientists if x.nobel is True))

# ================================================================================================================ map()
name_and_ages = tuple(map(
    lambda x: {'name': x.name, 'age': 2019 - x.born},
    scientists
))
pprint(name_and_ages)

# list comprehension
x = tuple({'name': x.name, 'age': 2017 - x.born} for x in scientists)
pprint(x)

# ============================================================================================================= reduce()
from functools import reduce

# get the total age of all the scientists
total_age = reduce(lambda acc, val: acc + val['age'], name_and_ages, 0)
print(total_age)

xx = sum(x['age'] for x in name_and_ages)
print(xx)


def reducer(acc, val):
    acc[val.field].append(val.name)
    return acc


scientists_by_field = reduce(reducer, scientists, {'math': [], 'physics': [], 'chemistry': [], 'astronomy': []})
pprint(scientists_by_field)

# can do the same using collections.defaultdict, this will automatically create a key and append a value to it
import collections
scientists_by_field = reduce(reducer, scientists, collections.defaultdict(list))
pprint(scientists_by_field)

