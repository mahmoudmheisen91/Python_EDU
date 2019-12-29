# DRY Donot Repeat Yourself
# WET Write Everything Twice / We Enjoy Typing

# functions
def fun1():
    print("hello world")

fun1()

def fun2(x, y):
    return x + y

print(fun2(1, 2))

def multiply(x, y):
    return x * y

# functions as arguments:
a = 4
b = 7
operation = multiply
print(operation(a, b))

def add(x, y):
  return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y))

# functions as objects:
a = 5
b = 10

print(do_twice(add, a, b))

def square(x):
    return x * x

def test(func, x):
    print(func(x))

test(square, 5)

# Modules:
import random

for i in range(5):
   value = random.randint(1, 6)
   print(value)

from math import pi, sqrt
print(pi)
# from math import *

from math import sqrt as square_root
print(square_root(100))

"""
Standard library's useful modules include string, 
re, datetime, math, random, os, multiprocessing, 
subprocess, socket, email, json, doctest, 
unittest, pdb, argparse and sys.

Tasks that can be done by the standard 
library include string parsing, data 
serialization, testing, debugging and 
manipulating dates, emails, command line 
arguments, and much more!

Some of the modules in the standard library 
are written in Python, and some are written in C.

pip install library_name
Using pip is the standard way of installing 
libraries on most operating systems, but some
libraries have prebuilt binaries for Windows.
These are normal executable files that let you 
install libraries with a GUI the same way you 
would install other programs.

PyPI Python Package Index
"""























