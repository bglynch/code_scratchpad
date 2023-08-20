# f-strings

###### Numbers

```py
In [1]: number = 800

# basic
In [2]: print(f"The number is {number}")
The number is 800

# hexidecimal representation of the number
In [3]: print(f"The number is {number:x}")
The number is 320

# scientific representation
In [4]: print(f"The number is {number:e}")
The number is 8.000000e+02

# leading zeros
In [6]: print(f"The number is {number:06}")
The number is 000800

# decimal places, 'f' stands for floating point
In [9]: print(f"The number is {200.12345:.2f}")
The number is 200.12

# add comma seperator to large numbers, seperator can be changed
In [10]: print(f"The number is {44000000000:,.2f}")
The number is 44,000,000,000.00

# print percentage from decimal
In [12]: print(f"The number is {0.34567:%}")
The number is 34.567000%

# print percentage from decimal, controlling decimal places
In [15]: print(f"The number is {0.34567:.2%}")
The number is 34.57%
```

###### Padding and Alignment

```py
# right align numbers
In [21]: for num in range(8,12): print(f"The number is {num:4}")
The number is    8
The number is    9
The number is   10
The number is   11

# right align text
In [23]: print(f"{'Hi':>6}")
    Hi

# align to center
In [24]: print(f"{'Hi':^6}")
  Hi
  
# align to left
In [25]: print(f"{'Hi':<6}")
Hi

# align to left, and choose what the padding symbol is
In [27]: print(f"{'Hi':_<6}")
Hi____
```

###### Datetime

```py
import datetime
today = datetime.datetime.now()

# basic
In [34]: print(f"the date is {today}")
the date is 2023-02-16 15:16:41.753612

# time only
In [35]: print(f"the date is {today:%H:%M}")
the date is 15:16

# time with seconds and milliseconds
In [38]: print(f"the date is {today:%H:%M:%S.%f}")
the date is 15:16:41.753612

# date only
In [42]: print(f"the date is {today:%y/%m/%d}")
the date is 23/02/16

# weekday 
In [43]: print(f"the date is {today:%A}")
the date is Thursday

# day month year
In [45]: print(f"the date is {today:%A, %b %d, %Y}")
the date is Thursday, Feb 16, 2023

# date according to current local
In [46]: print(f"the date is {today:%x}")
the date is 02/16/23
```

###### Printing variables

```py
x, y = 45, 78

# basic
In [49]: print(f"x={x}, y={y}")
x=45, y=78

# shortcut
In [52]: print(f"{x=}, {y=}")
x=45, y=78

# shortcut, with whitespaces 
In [53]: print(f"{x = }, {y = }")
x = 45, y = 78
```

