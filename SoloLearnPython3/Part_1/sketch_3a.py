# Functions:
def my_func(x, y):
	return x - y
	
print(my_func(2,3))

# functions as arguments:
def add(a, b):
	return a + b
	
func = add
print(func(1, 2))

# Functions as objects:
def add_one(x):
	return x + 1
	
def do2(func,a):
	return func(func(a))

num = 4
num2 = do2(add_one, num)
print(num2)

# Modules:
import random
print(random.randint(1, 5)) # 5 is included

from math import pi as pipi
print(pipi)

import unittest
print(dir(unittest))
