"""
Object Lifecycle

The lifecycle of an object is made up of its creation, manipulation, 
and destruction.

The first stage of the life-cycle of an object is the definition of 
the class to which it belongs.
The next stage is the instantiation of an instance, when __init__ is called. 
Memory is allocated to store the instance. Just before this occurs, 
the __new__ method of the class is called. This is usually overridden 
only in special cases.
After this has happened, the object is ready to be used.
"""

"""
When an object is destroyed, the memory allocated to it is freed up, and can be used for other purposes.
Destruction of an object occurs when its reference count reaches zero. Reference count is the number 
of variables and other elements that refer to an object.
If nothing is referring to it (it has a reference count of zero) nothing can interact with it, so it 
can be safely deleted.

In some situations, two (or more) objects can be referred to by each other only, and therefore can be deleted as well.
The del statement reduces the reference count of an object by one, and this often leads to its deletion.
The magic method for the del statement is __del__.
The process of deleting objects when they are no longer needed is called garbage collection.
In summary, an object's reference count increases when it is assigned a new name or placed in a container 
(list, tuple, or dictionary). The object's reference count decreases when it's deleted with del, 
its reference is reassigned, or its reference goes out of scope. When an object's reference 
count reaches zero, Python automatically deletes it.
"""

"""
A key part of object-oriented programming is encapsulation, which involves packaging of related variables 
and functions into a single easy-to-use object - an instance of a class.
A related concept is data hiding, which states that implementation details of a class should be hidden, 
and a clean standard interface be presented for those who want to use the class.
In other programming languages, this is usually done with private methods and attributes, which block 
external access to certain methods and attributes in a class.

The Python philosophy is slightly different. It is often stated as "we are all consenting adults here",
 meaning that you shouldn't put arbitrary restrictions on accessing parts of a class. Hence there are no 
 ways of enforcing a method or attribute be strictly private.
However, there are ways to discourage people from accessing parts of a class, such as by denoting that
 it is an implementation detail, and should be used at their own risk.
"""

"""
Weakly private methods and attributes have a single underscore at the beginning.
This signals that they are private, and shouldn't be used by external code. However, it is mostly 
only a convention, and does not stop external code from accessing them.
Its only actual effect is that from module_name import * won't import variables that start with a single underscore.
Example:
"""


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

"""
Strongly private methods and attributes have a 
double underscore at the beginning of their names. 
This causes their names to be mangled, which means 
that they can't be accessed from outside the class.
The purpose of this isn't to ensure that they are 
kept private, but to avoid bugs if there are
 subclasses that have methods or attributes 
 with the same names.
Name mangled methods can still be accessed 
externally, but by a different name. 
The method __privatemethod of class Spam could 
be accessed externally with _Spam__privatemethod.
"""


class Spam:
    __egg = 7

    def print_egg(self):
        print(self.__egg)


s = Spam()
s.print_egg()
print(s._Spam__egg)
# print(s.__egg)

'''
Basically, Python protects those members by 
internally changing the name to include the class name.
'''

"""
Methods of objects we've looked at so far are 
called by an instance of a class, which is then 
passed 
to the self parameter of the method.
Class methods are different - they are called by
 a class, which is passed to the cls 
 parameter of the method.
A common use of these are factory methods, 
which instantiate an instance of a class, 
using different parameters than those usually 
passed to the class constructor.
Class methods are marked with a classmethod decorator.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)


square = Rectangle.new_square(5)
print(square.calculate_area())

'''
new_square is a class method and is called on the 
class, rather than on an instance of the class. 
It returns a new object of the class cls.
'''
'''
Technically, the parameters self and cls are 
just conventions; they could be changed to 
anything else. However, they are universally 
followed, so it is wise to stick to using them.
'''

"""
Static methods are similar to class methods, 
except they don't receive any additional arguments; 
they are identical to normal functions that belong 
to a class.
They are marked with the staticmethod decorator.

Static methods behave like plain functions, 
except for the fact that you can call them 
from an instance of the class.
"""


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


"""
Properties provide a way of customizing access 
to instance attributes.
They are created by putting the property decorator
 above a method, which means when the instance 
 attribute with the same name as the method 
 is accessed, the method will be called instead.
One common use of a property is to make an 
attribute read-only.
"""


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
#pizza.pineapple_allowed = True

"""
Properties can also be set by defining setter/getter 
functions.
The setter function sets the corresponding 
property's value.
The getter gets the value.
To define a setter, you need to use a decorator 
of the same name as the property, 
followed by a dot and the setter keyword.
The same applies to defining getter functions.
"""


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
#pizza.pineapple_allowed = True
# print(pizza.pineapple_allowed)

# simple game:
"""
def get_input():
  command = input(": ").split()
  verb_word = command[0]
  if verb_word in verb_dict:
    verb = verb_dict[verb_word]
  else:
    print("Unknown verb {}". format(verb_word))
    return

  if len(command) >= 2:
    noun_word = command[1]
    print (verb(noun_word))
  else:
    print(verb("nothing"))

def say(noun):
  return 'You said "{}"'.format(noun)

verb_dict = {
  "say": say,
}

while True:
  get_input()


class GameObject:
  class_name = ""
  desc = ""
  objects = {}

  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self

  def get_desc(self):
    return self.class_name + "\n" + self.desc

class Goblin(GameObject):
  class_name = "goblin"
  desc = "A foul creature"

goblin = Goblin("Gobbly")

def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)

class Goblin(GameObject):
  def __init__(self, name):
    self.class_name = "goblin"
    self.health = 3
    self._desc = " A foul creature"
    super().__init__(name)

  @property
  def desc(self):
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "It has a wound on its knee."
    elif self.health == 1:
      health_line = "Its left arm has been cut off!"
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
    self._desc = value

def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    if type(thing) == Goblin:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed the goblin!"
      else: 
        msg = "You hit the {}".format(thing.class_name)
  else:
    msg ="There is no {} here.".format(noun) 
  return msg
"""

# Why was desc turned into a property?
# So it could be dynamically created when accessed


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
