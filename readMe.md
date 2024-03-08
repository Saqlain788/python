# Installation

    * Anaconda

# Hello World

    * Windows->Anconda prompt -> python
    ``````
    print('Hello World')
    ``````
    * open VS code -> hello_world.py
    ``````
    print('Hello World')
    ``````
    * intall python extension ->
    * click on run button ->

# create a new environment

    * conda create -n python123 python==3.12 -y
    * conda activate python123
    * pip install -r requirements.txt

# String Methods:

    # Boundaries
        * 'string text' single quote
        * "string text" double quote
        * '''string text''' triple single quote
        * """string text""" triple double quote

# Define Multiline string """ text string """

# Function and attributes

    * Print()
    * Print(id())
    * Print(type())
    * dir(str)
    * len()

# String Methods command dir(str)

    #* [i for i in dir(str) if "__" not in i]
    * Lowercase -> lower()
    * Uppercase -> upper()
    * Capitalize -> capitalize()
    * format -> format(a, b)

# Generate Table

    * !conda install lxml -y
    * import pandas as pd

table = pd.read_html('http://www.w3schools.com/python/python_operators.asp')

    * table[0]

# Ascii Code

    * A = 65     ** ord ('A')
    * Z = 90     ** chr(65)

    * a = 97
    * z = 122

    * 0 = 48
    * 9 = 57

# \*\*: Exponentiation

## //: Floor division

# Logical Operators

    * AND operator means لازمی
    * OR  operator means OPTIONAL
    * & | symbols are used in binary (pandas)

# Identity Operators

    * X is Z as physical address is same
    * (is) or (is not) operator checking memory (RAM) at low level
    * = or != operator checking value level

# Unzip

    * put * symbol before value
    data = ('ali', 2, 3.4)
    print(*data)

# List

    * dynamic length
    * hetrogenous data types (Multiple type)
    * index
        * postive (left to right)   0 to n-1
        * negative (right to left) -1 to length
    * slicing
        * variable names[start:end:step]
        * start : int = include
        * end : int = n-1
        * step : int = sequance
        * default slicing go from left to right
    * List is also a function i.e. list('abc') for performing iteration over items.

# List Methods

- [i for i in dir(list) if "__" not in i]

## del()

- variable_name.del() // delete element / object from memory

## POP()

- variable_name.pop() // delete last element
- variable_name.pop(2) // delete particular element

## Append()

- variable_name.append() // add element at last of list

## Insert(1,"Rashid)

- variable_name.insert() // add element at particular position of list

## Clear()

- variable_name.clear() // remove all elements from list / object, however, emply object will be reflected.

## Clear()

- variable_name.clear() // remove all elements from list / object, however, emply object will be reflected.

* ['append','clear','copy','count','extend','index','insert','pop','remove','reverse','sort']

# Help

    * help(object)
    * object?
    * object??
    * ?object
    * ??object

# Class 05

List

- iteration operation with for loop
  # for name in names:
  # print(name)
- apply any operation on element

# For Loop

- A for loop in Python is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

- Example:
  fruits = ["apple", "banana", "cherry"]
  for x in fruits:
  print(x)

## For Loop iteration on first 5 elements is possible by slicing methods

for name in names[:2]:
print(name)

# Number with Loop

- Range (start,end,step)
- range and enumerate are generative function having benefit of being used in memory.
- range is performed with iteration i.e.

# List Comprehensive

```
    for item in items_list:
    loop_body
```

- Comprehensive Style

```
[loop_body for item in items_list]

loop body used before forloop
and colon (:) will be omitted

```

# Jupyter Notebook return last line whereas PY file always use print function.

# Tuples is immutable neither add nor remove and update value.

# If Statement

```
x: int = 10
if x > 5:
    print("x is greater than 5")
```

## If-Else Statement

```
x: int = 4
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

## If-Elif-Else Statement

```
x: int = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

### Nested If-Else-Elif

```
x: int = 10
y: int = 5
if x > 5:
    if y > 5:
        print("x and y are both greater than 5")
    else:
        print("x is greater than 5 but y is not")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

# Static Type Variables

In Python 3.6 and later, you can use static type annotations to indicate the expected type of a variable.

```
x: int = 10
y: str = "Hello"
z: float = 3.14
Union and Optional Types
Union allows a variable to be one of several types. Optional is a shorthand for Union[T, None].

from typing import Union, Optional

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, Guest!"
    else:
        return f"Hello, {name}!"

age: Union[int, str] = "Twenty"
print(greet())
print(greet("John"))
```

# Zip Function with Lists

```
The zip function is used to combine two or more iterables.

names: list[str] = ["Alice", "Bob", "Charlie"]
ages: list[int] = [25, 30, 35]

zipped = zip(names, ages)
for name, age in zipped:
    print(f"{name} is {age} years old")
```

# Sorting a List of Tuples

```
You can sort a list of tuples based on the second tuple index using the sorted function.

tuples: list[tuple[str, int]] = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30)]
```

# If-else-elif

```
if logic:
    True_block
else:
    False_block
```

# comprehensive if-else

```
True_block if logic else False_block
if
if-else
if-elif-else
```

# comparison operators

```
==
>=
<=
!=
```

- logic

```
and
or
not
```

# Pip sign ( | ) Union Type

- To store more than one data type

# ZIP

- list(zip(data))

# Dictionary

- key:value (items)
  - key replacement of indexes
  - value item

* dict_variable[key]
  - dict_variable[new_key] = new_value
  - add new value
  - update value

# Set Data Type return unique and order elements. it is used in curly braces {}

# Setting up Static Typing

- To use static typing in Python, we'll need to import the required types from the typing module. For this guide, we're specifically interested in Any, Optional, and Union.

* from typing import Any, Optional, Union

# Creating Dictionaries

## Using Any Type

Any is the most flexible type. It can represent any type at all. Here's how to create a dictionary with keys of any hashable type and values of any type:

- from typing import Dict

```
my_dict: Dict[Any, Any] = {
1: "one",
"two": 2,
(3, 4): [3, 4]
}
```

## Using Optional Type

```
Optional is a shorthand for a value that can either be of a specific type or None.
```

- from typing import Dict

my_optional_dict: Dict[Any, Optional[int]] = {
1: 10,
"two": None,
(3, 4): 34
}

## Using Union Type

```
Union type allows us to specify that a value can be one of several types.

* from typing import Dict

my_union_dict: Dict[Any, Union[int, str]] = {
    1: "one",
    "two": 2,
    (3, 4): "three-four"
}
```

# Dictionary Comprehensions

- Dictionary comprehensions provide a concise way to create dictionaries.

```
squared_numbers = {i: i**2 for i in range(5)}
```

# Swapping Keys and Values

```
To swap the keys and values of a dictionary:

swapped_dict = {v: k for k, v in my_dict.items()}
```

# Error in Dictionary

- We cannot write dictionary {}, list[], tuples() and set{} as a key in the dictionary. However, we write these above mentioned as a values in the dictionary.
