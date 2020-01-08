# lambda
def my_func(f, arg):
  return f(arg)

print(my_func(lambda x: x * 2, 3))
print((lambda x: x + x)(4))

double = lambda x: x * 2
print(double(7))

# map, filter return iterable:
li = [11, 22, 33, 44, 55]

# cast to list:
result = list(map(lambda x: x+5, li))
print(result)

# filter
# predicate (a function that returns a Boolean).
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)
print("---------------")

# generator:
# type of iterable
'''
Unlike lists, they don't allow indexing with 
arbitrary indices, but they can still be iterated
 through with for loops.
They can be created using functions and the yield
statement.

generators allow you to declare a function 
that behaves like an iterator, i.e. it can be 
used in a for loop.
'''
def countdown():
  i=5
  while i > 0:
    yield i
    i -= 1
    
for i in countdown():
  print(i)

# transform gen to a list
def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11)))

def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

print_text = decor(print_text)
print_text()

@decor
def print_text2():
  print("Hello world! 2")

print_text2()

# recursion:
def factorial(x):
  if x == 1:
    return 1
  else: 
    return x * factorial(x-1)
    
print(factorial(5))

def is_even(x):
  if x == 0:
    return True
  else:
    return is_odd(x-1)

def is_odd(x):
  return not is_even(x)


print(is_odd(17))
print(is_even(23))

def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))

num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)

"""
Sets differ from lists in several ways, but share several list operations such as len.
They are unordered, which means that they can't be indexed.
They cannot contain duplicate elements.
Due to the way they're stored, it's faster to check whether an item is part of a set, rather than part of a list.
Instead of using append to add to a set, use add.
The method remove removes a specific element from a set; pop removes an arbitrary element.

Basic uses of sets include membership testing and the elimination of duplicate entries.
"""

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)


"""
Sets can be combined using mathematical operations.
The union operator | combines two sets to form a new one containing items in either.
The intersection operator & gets items only in both.
The difference operator - gets items in the first set but not in the second.
The symmetric difference operator ^ gets items in either set, but not both.
"""

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

"""
As we have seen in the previous lessons, Python supports the following data structures: lists, dictionaries, tuples, sets.

When to use a dictionary:
- When you need a logical association between a key:value pair.
- When you need fast lookup for your data, based on a custom key.
- When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
- Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
- Use a set if you need uniqueness for the elements.
- Use tuples when your data cannot change.
Many times, a tuple is used in combination with a dictionary, for example, a tuple might represent a key, because it's immutable.
"""

# itertools:
"""
The module itertools is a standard library that contains several functions that are useful in functional programming.
One type of function it produces is infinite iterators.
The function count counts up infinitely from a value.
The function cycle infinitely iterates through an iterable (for instance a list or string).
The function repeat repeats an object, either infinitely or a specific number of times.
"""
from itertools import count

for i in count(3):
  print(i)
  if i >=11:
    break

"""
There are many functions in itertools that operate on iterables, in a similar way to map and filter.
Some examples:
takewhile - takes items from an iterable while a predicate function remains true;
chain - combines several iterables into one long one;
accumulate - returns a running total of values in an iterable.
"""

from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))

"""
There are also several combinatoric functions in itertool, such as product and permutation.
These are used when you want to accomplish a task with all possible combinations of some items.
"""
from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters))) 

from itertools import product
a={1, 2}
print((list(product(range(3), a))))









































