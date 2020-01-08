# Dicitionary:
dic = {
    "one": 1,
    "two": 2,
    "three": 3,
}
print(dic["one"])

dic["four"] = 4
dic[5] = 6
print(dic)

print(6 in dic)
print(5 in dic)
print(dic.get("one"))
print(dic.get(7, "do not exists"))
print(8*"-")

# Tubles:
tup = (1, 2, 3, 4)
print(tup[1])

tup = 1, 2, 3, 4, 4
print(tup)

tup = (1,)
print(tup)

nums = (55, 44, 33, 22)
print(max(min(nums[0:2]), abs(-42)))
print(8*"-")

# Lists:
s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(s[1:3])
print(s[:4])
print(s[5:])  # 9 will print
print(s[:4:-1])
print(s[5::-1])
print(s[-13:-1])
print(8*"-")

a = [i**2 for i in range(5)]
print(a)

b = [i**2 for i in range(6) if i % 2 == 0]
print(b)
print(8*"-")

print(max([1, 4, 9, 2, 5, 6, 8]))
print(sum([1, 2, 3, 4, 5]))
print(8*"-")

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

a = [i for i in range(10)]
a_bool = [i % 2 == 0 for i in a]
print(a_bool)
print(any(a_bool))

for v in enumerate(nums):
    print(v)
print(8*"-")

# String:
a = [1, 2]
msg1 = "nums: {0}, {1}".format(a[0], a[1])
msg2 = "numx: {x}, {y}".format(y=6, x=33)
print(msg1)
print(msg2)

print(", ".join(["spam", "eggs", "ham"]))
print("Hello ME".replace("ME", "world"))
print("This is a sentence.".startswith("This"))
print("This is a sentence.".endswith("sentence."))
print("this is a sentence.".upper())
print("AN ALL CAPS SENTENCE".lower())
print("spam, eggs, ham".split(", "))
print(8*"-")
