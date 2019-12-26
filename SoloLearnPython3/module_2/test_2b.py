# while loop:
i = 3
while i>=0:
    print(i)
    i = i - 1
print("---------------")

# infinite, breaking:
i = 6
while True:
    i = i - 1
    if i == 3:
        print("skipping 3")
        continue
      
    if i <= 2:
        print("breaking at 2")
        break

    print(i)
print("---------------")

# lists:
nums = [5, 4, 3, 2, 1]
print(nums[1])

# list operations
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print("---------------")

nums = [1, 2, 3]
nums.append(4)
print(nums)
print(len(nums))
nums.insert(1, 5)
print(nums)
print(nums.index(5))
print("---------------")

numbers = list(range(10))
print(numbers)

numbers = list(range(5, 10))
print(numbers)

nums = list(range(3, 15, 3))
print(nums)
print("---------------")

# for loops:
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

# simple calculator:
"""
while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")

   if user_input == "quit":
      break
   elif user_input == "add":
      ...
   elif user_input == "subtract":
      ...
   elif user_input == "multiply":
      ...
   elif user_input == "divide":
      ...
   else:
      print("Unknown input")
"""