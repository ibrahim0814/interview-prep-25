# Python Primitives & Essentials Reference

## Basic Data Types

```python
# Numbers
x = 42                    # int
y = 3.14                  # float
z = 2 + 3j                # complex

# Boolean
is_true = True
is_false = False

# None
empty = None

# Type checking
type(x)                   # <class 'int'>
isinstance(x, int)        # True
```

## Strings

```python
# Creation
s = "hello"
s = 'hello'
s = """multiline
string"""
s = f"formatted {x}"      # f-string
s = "value: {}".format(x) # .format()
s = "value: %d" % x       # % formatting

# Operations
len(s)                    # length
s[0]                      # indexing
s[-1]                     # last character
s[1:4]                    # slicing
s[:3]                     # first 3
s[2:]                     # from index 2
s[::-1]                   # reverse

# Methods
s.upper()                 # HELLO
s.lower()                 # hello
s.capitalize()            # Hello
s.title()                 # Hello World
s.strip()                 # remove whitespace
s.replace('l', 'x')       # hexxo
s.split(',')              # split by delimiter
','.join(['a', 'b'])      # join list to string
s.startswith('he')        # True
s.endswith('lo')          # True
s.find('ll')              # index of substring (-1 if not found)
s.count('l')              # count occurrences
s.isdigit()               # check if all digits
s.isalpha()               # check if all letters
```

## Lists

```python
# Creation
lst = []
lst = [1, 2, 3]
lst = list(range(5))      # [0, 1, 2, 3, 4]
lst = [x for x in range(5)] # list comprehension

# Operations
len(lst)                  # length
lst[0]                    # indexing
lst[-1]                   # last element
lst[1:3]                  # slicing
lst[:2]                   # first 2
lst[2:]                   # from index 2

# Methods
lst.append(4)             # add to end
lst.insert(0, 'first')    # insert at index
lst.extend([5, 6])        # add multiple
lst.remove(2)             # remove first occurrence
lst.pop()                 # remove and return last
lst.pop(0)                # remove and return at index
lst.clear()               # remove all
lst.reverse()             # reverse in place
lst.sort()                # sort in place
lst.sort(reverse=True)    # sort descending
sorted(lst)               # return new sorted list
lst.index(2)              # find index of value
lst.count(2)              # count occurrences
lst.copy()                # shallow copy

# Checking
if 2 in lst:
    pass
if 2 not in lst:
    pass
```

## Tuples

```python
# Creation
tup = ()
tup = (1,)                # single element (comma needed)
tup = (1, 2, 3)
tup = 1, 2, 3             # parentheses optional

# Operations
len(tup)                  # length
tup[0]                    # indexing
tup[1:3]                  # slicing
tup.count(1)              # count occurrences
tup.index(2)              # find index

# Unpacking
a, b, c = tup
a, *rest, c = tup         # starred expression
```

## Sets

```python
# Creation
s = set()
s = {1, 2, 3}
s = set([1, 2, 3])

# Operations
len(s)                    # size
s.add(4)                  # add element
s.update([5, 6])          # add multiple
s.remove(2)               # remove (raises KeyError if not found)
s.discard(2)              # remove (no error if not found)
s.pop()                   # remove and return arbitrary element
s.clear()                 # remove all
s.copy()                  # shallow copy

# Set operations
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.union(s2)              # {1, 2, 3, 4, 5} or s1 | s2
s1.intersection(s2)       # {3} or s1 & s2
s1.difference(s2)         # {1, 2} or s1 - s2
s1.symmetric_difference(s2) # {1, 2, 4, 5} or s1 ^ s2
s1.issubset(s2)           # False
s1.issuperset(s2)         # False

# Checking
if 2 in s:
    pass
if 2 not in s:
    pass
```

## Dictionaries/Maps

```python
# Creation
d = {}
d = {'key': 'value'}
d = dict(key='value')
d = dict([('a', 1), ('b', 2)])

# Operations
d['key'] = 'value'        # set item
d['key']                  # get item (KeyError if not found)
d.get('key')              # get item (None if not found)
d.get('key', 'default')   # get with default
d.setdefault('key', 'default') # get or set default
del d['key']              # delete item
d.pop('key')              # remove and return
d.pop('key', 'default')   # pop with default
d.popitem()               # remove and return arbitrary item
d.clear()                 # remove all
d.copy()                  # shallow copy
d.update({'new': 'value'}) # update with another dict

# Views
d.keys()                  # dict_keys object
d.values()                # dict_values object
d.items()                 # dict_items object
list(d.keys())            # convert to list

# Checking
if 'key' in d:
    pass
if 'key' not in d:
    pass

# Iteration
for key in d:
    pass
for key, value in d.items():
    pass
```

## Control Flow

```python
# If statements
if condition:
    pass
elif other_condition:
    pass
else:
    pass

# Ternary operator
result = value_if_true if condition else value_if_false

# For loops
for i in range(5):        # 0 to 4
    pass
for i in range(2, 8):     # 2 to 7
    pass
for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    pass

for item in lst:
    pass
for i, item in enumerate(lst):
    pass
for key, value in d.items():
    pass

# While loops
while condition:
    pass

# Loop control
for i in range(10):
    if i == 3:
        continue          # skip to next iteration
    if i == 7:
        break             # exit loop
else:
    pass                  # executes if loop completed normally
```

## Functions

```python
# Basic function
def func_name(param1, param2):
    return param1 + param2

# Default parameters
def func(param1, param2='default'):
    return param1 + param2

# Variable arguments
def func(*args):          # tuple of arguments
    return sum(args)

def func(**kwargs):       # dictionary of keyword arguments
    return kwargs['key']

def func(*args, **kwargs):
    pass

# Lambda functions
square = lambda x: x ** 2
add = lambda x, y: x + y

# Map, filter, reduce
list(map(square, [1, 2, 3]))        # [1, 4, 9]
list(filter(lambda x: x > 2, [1, 2, 3, 4])) # [3, 4]
from functools import reduce
reduce(lambda x, y: x + y, [1, 2, 3, 4])    # 10
```

## List Comprehensions & Generators

```python
# List comprehensions
squares = [x**2 for x in range(5)]           # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]
matrix = [[j for j in range(3)] for i in range(3)]

# Dictionary comprehensions
squares_dict = {x: x**2 for x in range(5)}

# Set comprehensions
unique_squares = {x**2 for x in range(-5, 6)}

# Generator expressions
squares_gen = (x**2 for x in range(5))       # generator object
```

## Exception Handling

```python
try:
    risky_operation()
except ValueError as e:
    print(f"ValueError: {e}")
except (TypeError, KeyError):
    print("Multiple exception types")
except Exception as e:
    print(f"Any other exception: {e}")
else:
    print("No exception occurred")
finally:
    print("Always executes")

# Raising exceptions
raise ValueError("Custom error message")
raise                     # re-raise current exception
```

## Classes (Basic)

```python
class MyClass:
    class_variable = "shared"
    
    def __init__(self, value):
        self.instance_variable = value
    
    def method(self):
        return self.instance_variable
    
    @classmethod
    def class_method(cls):
        return cls.class_variable
    
    @staticmethod
    def static_method():
        return "static"

# Usage
obj = MyClass("value")
obj.method()
MyClass.class_method()
MyClass.static_method()
```

## Common Built-in Functions

```python
# Type conversion
int("123")                # 123
float("3.14")             # 3.14
str(123)                  # "123"
bool(1)                   # True
list("hello")             # ['h', 'e', 'l', 'l', 'o']
tuple([1, 2, 3])          # (1, 2, 3)
set([1, 2, 2, 3])         # {1, 2, 3}

# Math
abs(-5)                   # 5
min(1, 2, 3)              # 1
max(1, 2, 3)              # 3
sum([1, 2, 3])            # 6
round(3.14159, 2)         # 3.14
pow(2, 3)                 # 8 (same as 2**3)

# Iteration
len(obj)                  # length
enumerate([a, b, c])      # [(0, a), (1, b), (2, c)]
zip([1, 2], ['a', 'b'])   # [(1, 'a'), (2, 'b')]
reversed([1, 2, 3])       # [3, 2, 1]
sorted([3, 1, 2])         # [1, 2, 3]
all([True, True, False])  # False
any([True, False, False]) # True

# Object info
type(obj)                 # object type
isinstance(obj, str)      # type checking
hasattr(obj, 'attr')      # check if attribute exists
getattr(obj, 'attr', 'default') # get attribute with default
dir(obj)                  # list attributes and methods
```

## File I/O

```python
# Reading files
with open('file.txt', 'r') as f:
    content = f.read()           # read entire file
    lines = f.readlines()        # read all lines as list
    line = f.readline()          # read one line

# Writing files
with open('file.txt', 'w') as f:
    f.write('content')
    f.writelines(['line1\n', 'line2\n'])

# File modes: 'r' (read), 'w' (write), 'a' (append), 'x' (create)
# Add 'b' for binary mode: 'rb', 'wb'
```

## Common Patterns

```python
# Swapping variables
a, b = b, a

# Multiple assignment
a = b = c = 0

# Chained comparisons
if 0 < x < 10:
    pass

# Default dictionary
from collections import defaultdict
dd = defaultdict(list)
dd['key'].append('value')  # creates list automatically

# Counter
from collections import Counter
counts = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
# Counter({'a': 3, 'b': 2, 'c': 1})

# Unpacking
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2, 3, 4], last=5
```