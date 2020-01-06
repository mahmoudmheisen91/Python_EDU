# Try except:
try:
    print(10)
    print(3/0)
except ZeroDivisionError:
    print("error")
except (ZeroDivisionError, ValueError):
    print("two errors")
except:
    print("all")
finally:
    print("always run")
print(5*"-")

# Assertion:
print(0)
assert 1 == 1
print(1)
assert 2 == 2
print(2)

try:
    assert 2 == 1  # Assertion error
except AssertionError:
    print("Assertion Error")
finally:
    num = 3  # Assertion Message
    #assert (num < 0), "num is +ve"


def add(num1, num2):
    assert type(num1) == int, "num1 must be int"
    assert type(num2) == int, "num1 must be int"
    assert num1 >= 0, "num1 must be +ve"
    assert num2 >= 0, "num2 must be +ve"
    return num1 + num2


#print(add(4.2, -5))
assert add(2, 3) == 5

# Raise:
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
