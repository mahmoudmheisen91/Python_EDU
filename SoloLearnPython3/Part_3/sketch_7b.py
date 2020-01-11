# Private:
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)


queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

# Mangled:


class Spam:
    __egg = 7

    def print_egg(self):
        print(self.__egg)


s = Spam()
s.print_egg()
print(s._Spam__egg)

# Class Method:


class Rect:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w*self.h

    @classmethod
    def square2(cls, side):
        return cls(side, side)


sq = Rect.square2(3)
print(sq.area())


# Static method:
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True


ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

# Property:


class Pizza2:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    # make read only
    @property
    def pineapple_allowed(self):
        print("test")
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        password = "a"
        if password == "a":
            self._pineapple_allowed = value
        else:
            raise ValueError("Alert! Intruder!")


p = Pizza2([1])
p.pineapple_allowed = True
print(p.pineapple_allowed)


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


p = Person(1)
print(p.name)
p.name = 2
print(p.name)
