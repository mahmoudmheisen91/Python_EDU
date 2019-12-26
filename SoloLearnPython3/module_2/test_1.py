# booleans:
x = True
y = False
print(x==y)
print(x!=y)

# if else:
x = 4
if x > 2:
    print("bigger than 2")
elif x > 6:
    print("bigger than 6")
else:
    print("small")

# and or not
y = 1 == 1 and 2 == 2
print("y = " + str(y))

y = 1 == 1 or 2 == 2
print("y = " + str(y))

y = not 2 == 2
print("y = " + str(y))
