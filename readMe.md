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
