class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        fmt = "{0} is {1}".format(self.name, self.color)
        print(fmt)

myCat = Cat('Jack', 'Black')
myCat.show()
print("here i added print")

class Dog:
    legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color

fido = Dog("Fido", "brown")
print(fido.legs)
print(fido.name)
print(Dog.legs)
# print(Dog.name) # will not work

# inheritance
class Animal: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat2(Animal):
    def purr(self):
        print("Purr...")
        
class Dog2(Animal):
    def bark(self):
        print("Woof!")

fido = Dog2("Fido", "brown")
print(fido.color)
fido.bark()

# super method():
class A:
  def spam(self):
    print(1)

class B(A):
  def spam(self):
    print(2)
    super().spam()

B().spam()

# method override:
class Wolf: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Grr...")

class Dog3(Wolf):
  def bark(self):
    print("Woof")
        
husky = Dog3("Max", "grey")
husky.bark()


# Magic methods (dunders):
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

a = Vec2(1, 1)
b = Vec2(2, 2)
c = a + b # a + b is translated into a.__add__(b).

print(c.x)
print(c.y)


'''
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |
'''

'''
The expression x + y is translated into x.__add__(y).
However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called.
There are equivalent r methods for all magic methods just mentioned.
'''

class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

'''
Python also provides magic methods for comparisons.
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

If __ne__ is not implemented, it returns the opposite of __eq__.
There are no other relationships between the other operators.
'''

class SpecialString2:
  def __init__(self, cont):
    self.cont = cont

  def __gt__(self, other):
    for index in range(len(other.cont)+1):
      result = other.cont[:index] + ">" + self.cont
      result += ">" + other.cont[index:]
      print(result)

spam = SpecialString2("spam")
eggs = SpecialString2("eggs")
spam > eggs


"""
There are several magic methods for making classes act like containers.
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

There are many other magic methods that we won't cover here, such as __call__ for calling objects as functions, and __int__, __str__, and the like, for converting objects to built-in types.
"""

import random

class VagueList:
  def __init__(self, cont):
    self.cont = cont

  def __getitem__(self, index):
    return self.cont[index + random.randint(-1, 1)]

  def __len__(self):
    return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

a = input(": ")







































