# Itertools:
from itertools import chain, count, accumulate
from itertools import takewhile, product, permutations

for i in count(5):
    print(i)
    if i == 6:
        break

nums = list(accumulate(range(8)))
print(nums)
num2 = list(takewhile(lambda x: x <= 6, nums))
print(num2)
num3 = list(filter(lambda x: x <= 6, set(nums)))
print(num3)
print(list(chain(num2, num3)))

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters, 2)))

# Recursion:


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


print(factorial(6))


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


# Need memoization (socratica)
print(fib(4))


def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)  # not is_even(x-1)


def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(23))
print(8*"-")

"""
6435 Lakeview Blvd, APT#9204, Westland, MI, 
48185 (zip code)
"""

# Sets:
s1 = {1, 2, 2, 3, 4}
s2 = set([11, 22, 33, 44])
print(s1)
print(s2)
print(3 in s1)
print(3 in s2)

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)
nums.pop()
print(nums)

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)
