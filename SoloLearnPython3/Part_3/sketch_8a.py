import re

# raw:
print(r"I am \r\a\w!")
print("I am \r\a\w!")

# match, search, findall, sub:
pattern = r"spam"
print(re.match(pattern, "spamegg"))
print(re.match(pattern, "eggspam"))

print(re.search(pattern, "eggspamspam"))
print(re.search(pattern, "eggsp"))

print(re.findall(pattern, "eggspamsausagespam"))

matchsrch = re.search(pattern, "eggspamspam")
if matchsrch:
    print(matchsrch.group())
    print(matchsrch.start())
    print(matchsrch.end())
    print(matchsrch.span())

str = "My name is spam. Hi spam."
newstr = re.sub(pattern, "Amy", str)
print(newstr)

# metas:
# . any
# ^a start with a
# a$ end with a
# [aeiou] contains (character class)
# ^ inside character class means invert
# - range
# () group of characters
# * means "zero or more repetitions of the previous
# thing". The "previous thing" can be a single
# character, a class, or a group of
# characters in parentheses.
# + one or more repetitions
# ? means "zero or one repetitions".
# {} number of repetitions between two numbers.
# {0,1} is the same thing as ?.
# {1,} same as +
# {0,} sameas *
# | means or red|blue: either red or blue

# '([^aeiou][aeiou][^aeiou])+'
# the above mean One or more repetitions of a
# non-vowel, a vowel and a non-vowel

pattern = r"gr.y"
if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Match 3")

print(8*"-")

pattern = r"^gr.y$"
if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "stingray"):
    print("Match 3")

print(8*"-")

pattern = r"[aeiou]"
if re.search(pattern, "grey"):
    print("Match 1")

if re.search(pattern, "qwertyuiop"):
    print("Match 2")

if re.search(pattern, "rhythm myths"):
    print("Match 3")

print(8*"-")

pattern = r"[A-Z][A-Z][0-9]"
if re.search(pattern, "LS88"):
    print("Match 1")

if re.search(pattern, "E3"):
    print("Match 2")

if re.search(pattern, "1ab"):
    print("Match 3")

print(8*"-")

pattern = r"[^A-Z]"
if re.search(pattern, "this is all quiet"):
    print("Match 1")

if re.search(pattern, "AbCdEfG123"):
    print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")

print(8*"-")

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")

print(8*"-")

pattern = r"9{1,3}$"

if re.match(pattern, "99"):
    print("Match 1")

if re.match(pattern, "999"):
    print("Match 2")

if re.match(pattern, "9999"):
    print("Match 3")

print(8*"-")

pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print(match.group(4))
    print(match.groups())

print(8*"-")
