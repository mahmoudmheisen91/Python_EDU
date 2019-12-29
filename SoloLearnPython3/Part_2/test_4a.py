"""
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range 
number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an 
inappropriate type;
ValueError: a function is called on a value of 
the correct type, but with an inappropriate value.
"""

# try except:
try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")
print("---------------")

# all errors:
try:
   word = "spam"
   print(word / 0)
except:
   print("An error occurred")
print("---------------")

try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")
print("---------------")

"""
num = -3
if float(num) < 0:
    raise ValueError("Negative!")
"""

"""
try:
   num = 5 / 0
except:
   print("An error occurred")
   raise
"""

"""
Programmers often place assertions at the 
start of a function to check for valid input, 
and after a function call to check for valid 
output.
"""

"""
print(0)
assert "h" != "w"
print (1)
assert False
print(2)
"""

temp = -10
assert (temp >= 0), "Colder than absolute zero!"






















