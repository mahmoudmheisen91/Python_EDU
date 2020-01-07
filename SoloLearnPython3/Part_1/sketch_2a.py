# Logics:
x = True  # must be capital

if x and 3 == 3:
    print(str(not x))
else:
    print(str(False))

num = 4
if num > 10:
    print("biiger")
elif num > 2 or num != 5:
    print(f"{num} bigger than 2")
else:
    print("nop")

print(5*"-")

# while loop:
i = -1
while i < 10:
    i += 1
    if i == 5 or i == 6:
        continue
    if i == 8:
        break
    print(f"i = {i}")

print(10*"-")

# while and else no break:
i = 0
while i < 3:
    print(f"i = {i}")
    i += 1
else:
    print(10*"-")

# Lists:
li1 = []
li2 = list()
li3 = list([])

print(f"li1 = {li1}")
print(f"li2 = {li2}")
print(f"li3 = {li3}")

li1 = [1, 2, 3]
print(f"li1 = {li1}")
print(li1[0])

li2 = [4, 5]
print(f"li1+li2 = {li1+li2}")
print(f"li1*3 = {li1 * 3}")
print(3 in li1)
print(3 in li2)
print(3 not in li1)
print(not 3 in li2)

li1.append(4)
print(len(li1))
print(f"li1 = {li1}")
print(li1.index(4))
li1.insert(1, 5)
print(f"li1 = {li1}")
print(li1.index(4))

numbers = list(range(10))
print(numbers)

numbers = list(range(5, 10))
print(numbers)

nums = list(range(3, 15, 3))
print(nums)
print(10*"-")

# for loops:
for i in li1:
    print(str(i) + "!")

print(dir(list))

print(8*"-")
a = [1, 1, 2, 3]
print(max(a))
print(min(a))
print(a.reverse())
print(a)
print(a.count(1))
print(a.remove(1))
print(a)
