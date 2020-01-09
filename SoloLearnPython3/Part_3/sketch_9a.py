# Zen of python:
import this

# Functions:


def func1(narg, *arg):  # arg at the end
    print(narg)
    print(arg)


def func2(x, y, food="spam"):  # f at the end
    print(food)


def func3(x, y=7, *arg, **karg):  #
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"arg: {arg}")
    print(f"karg: {karg}")
    print(8*"-")


func1(2, 3, 4, 5)
func2(1, 2)
func2(3, 4, "egg")
func3(2, 3, 4, 5, a=6, b=7)
func3(2, a=6, b=7)
func3(2, 3, a=6, b=7)

# Unpacking:
a = (1)  # must be (1,)
b = (1, 2, 3)
x, y, z = b
x, y = y, x
print(x)
print(y)
print(z)
print(8*"-")

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

# Trenary operator:
a = 3 if 4 == 5 else 2
print(a)

# Else:
for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)

for i in range(6):
    try:
        if 5 / i == 1.0:
            break
    except ZeroDivisionError:
        print(1)
    else:
        print(2)

# Module:
if __name__ == "__main__":
    print("Hi")  # script
else:
    print("Welcome")  # module
