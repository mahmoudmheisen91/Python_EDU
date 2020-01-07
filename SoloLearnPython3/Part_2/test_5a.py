# dict:
primary = {
  "red": [255, 0, 0], 
  "green": [0, 255, 0], 
  "blue": [0, 0, 255], 
}

print(primary["red"])

"""
Only immutable objects can be used as keys to 
dictionaries. Immutable objects are those that 
can't be changed "string, tuple". So far, the only mutable 
objects you've come across are lists and 
dictionaries.
"""

squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)

nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))
print("---------------")

# Tuples are very similar to lists, except that 
# they are immutable (they cannot be changed)
words = ("spam", "eggs", "sausages",)
print(words[0])

my_tuple = "one", "two", "three"
print(my_tuple[0])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

print(squares[:7])
print(squares[7:])

print(squares[::2])
print(squares[2:8:3])
print("---------------")

# list comprehension:
cubes = [i**3 for i in range(5)]
print(cubes)

evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)
print("---------------")

# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)

a = "{x}, {y}".format(x=5, y=12)
print(a)
print("---------------")

print(", ".join(["spam", "eggs", "ham"]))
print("Hello ME".replace("ME", "world"))
print("This is a sentence.".startswith("This"))
print("This is a sentence.".endswith("sentence."))
print("This is a sentence.".upper())
print("AN ALL CAPS SENTENCE".lower())
print("spam, eggs, ham".split(", "))
print("---------------")

print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))
print("---------------")

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")

for v in enumerate(nums):
   print(v)

print("---------------")

# we can slice tuple:
nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
print("---------------")

# Text analyzer:
def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

filename = input("Enter a filename: ")
with open(filename) as f:
  text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))

























