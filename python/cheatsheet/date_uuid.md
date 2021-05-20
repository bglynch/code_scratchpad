# Python Dates and Time



## Time

```
import tim
```



```python
# unix time
time.time
>>> 1617361654.218611

time.time_ns()
>>> 1617361698038243000
```



### Function execution time

```python
import time
start_time = time.time()
main()
print(f"--- {(time.time() - start_time)} seconds ---")

--- 0.764891862869 seconds ---
```



## Date

[**ISO 8601**](https://en.wikipedia.org/wiki/ISO_8601) : International Organization for Standardization on Time



format

```
YYYY-MM-DD HH:MM:SS
```



```python
from datetime import date, time, datetime

date(year=2020, month=1, day=31)
>>> datetime.date(2020, 1, 31)

time(hour=13, minute=14, second=31)
>>> datetime.time(13, 14, 31)

datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31)
>>> datetime.datetime(2020, 1, 31, 13, 14, 31)
```



```python
date.today()
>>> datetime.date(2021, 4, 2)

now = datetime.now()
time(now.hour, now.minute, now.second)
```



### String to ```datetime```

```python
from datetime import date, datetime

date.fromisoformat("2020-01-31")
>>> datetime.date(2020, 1, 31)

date_string = "01-31-2020 14:45:37"
format_string = "%m-%d-%Y %H:%M:%S"

datetime.strptime(date_string, format_string)
>>> datetime.datetime(2020, 1, 31, 14, 45, 37)
datetime.strptime(date_string, format_string).date()
>>> datetime.date(2020, 1, 31)
```







## Create UID

uuid = universally unique identifier

guid = globally unique identifier



https://docs.python.org/3/library/hashlib.html#examples

```python
import hashlib
from hashlib import blake2b

length_of_uid = 4

'''
hashlib.blake2b(
	data=b'', *, digest_size=64, key=b'', salt=b'', person=b'', fanout=1, depth=1,
	leaf_size=0, node_offset=0, node_depth=0, inner_size=0, last_node=False,
	usedforsecurity=True)
'''
h = blake2b(digest_size=length_of_uid)
unique_key = "string".encode('utf-8')
h.update(unique_key)
uid = h.hexdigest()

uid = blake2b(b'Hello world', digest_size=5).hexdigest()

uid = hashlib.md5("str".encode('utf-8')).hexdigest()
```



