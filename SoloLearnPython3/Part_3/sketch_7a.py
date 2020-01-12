import random

# Class:
class Animal:
    id2 = 3

    def __init__(self, id):
        self.id = id

    def show(self):
        print(f"Animal: id= {self.id}")


c1 = Animal(3)
c2 = Animal(4)
c1.show()
c2.show()
print(Animal.id2)
print(c1.id)
print(c1.id2)
# print(Animal.id) # will not work
print(8*"-")

# Inheritance:


class Cat(Animal):
    def purr(self):
        print("purr...")

    # method override:
    def show(self):
        print("overriden")


class Dog(Animal):
    def bark(self):
        print("woff..")

    # super method:
    def show(self):
        print("Dog")
        super().show()


d1 = Dog(12)
d1.show()
d1.bark()
c1 = Cat(123)
c1.show()
print(8*"-")

# Magic Methods Dunders:
'''
__radd__
__new__
__del__
__repr__

__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in
for loops)
__contains__ for in
__call__ for calling objects as functions,
and __int__, __str__, for converting objects
to built-in types.
'''


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)


a = Vec2(1, 1)
b = Vec2(2, 2)
c = a + b  # a + b is translated into a.__add__(b).

print(c.x)
print(c.y)


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)


spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs


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
print(8*"-")

