# Lambda:
print((lambda x: x + 1)(3))

func1 = (lambda x: x + 1)
print(func1(2))


def func2(f, arg):
    return func2(arg)


print((lambda x: x+1)(4))

a = [1, 2, 3, 4, 5]
print(list(map(lambda x: x+3, a)))
print(list(filter(lambda x: x < 3, a)))

# Generator:
print("Generators")


def counter():
    i = 3
    while i > 0:
        yield i
        i -= 1


for i in counter():
    print(i)


def count2(x):
    for i in range(x):
        yield i


print(list(count2(5)))

# Decorators:


def dec(f):
    def wrap():
        print(8*"-")
        f()
        print(8*"-")
    return wrap  # not called


def print_text():
    print("Hello World")


func = dec(print_text)
func()

# or:
@dec
def print_text2():
    print("Hello World")


print_text2()
