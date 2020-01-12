import re

# (?P<name>...) named group
# (?:...) Non-capturing group
# \1 to 99 Special Sequence matches
# the expression of the group
# \d match digits [0-9]
# \D match non digits
# \s match spaces [ \t\n\r\f\v]
# \S match non spaces
# \w match word [a-zA-Z0-9_]
# \W match non word
# \A match beginning of string
# \Z match end of string
# \b match boundary between words
# \B match empty string anywhere else

# "123!456!" == [1-6!] == (\d*\W)+

# Which pattern would match 'SPAM!' in a search?
# \AS...\b.\Z

# "(4{5,6})\1" means 10 or 12 fours

pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

print(8*"-")

#pattern = r"(.+) (.+)"
pattern = r"(.+) \1"
match = re.match(pattern, "word word")
if match:
    print("Match 1")

match = re.match(pattern, "?! ?!")
if match:
    print("Match 2")

match = re.match(pattern, "abc cde")
if match:
    print("Match 3")

print(8*"-")

pattern = r"(\D+\d)"
match = re.match(pattern, "Hi 999!")
if match:
    print("Match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
    print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")

print(8*"-")

pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
    print("Match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
    print("Match 2")

match = re.search(pattern, "We scattered.")
if match:
    print("Match 3")

print(8*"-")

# Email Extraction
# dot followed by \ to treat it like character
'''
The regex above says that the string should contain 
a word (with dots and dashes allowed), 
followed by the @ sign, then another similar word, 
then a dot and another word.
'''
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"
match = re.search(pattern, str)
if match:
    print(match.group())
