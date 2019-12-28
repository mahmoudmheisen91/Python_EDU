import re

pattern = r"spam" #raw string, don't escape anything

if re.match(pattern, "spamspamspam"):
   print("Match")
else:
   print("No match")


pattern = r"spam"
if re.match(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")

if re.search(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")
    
print(re.findall(pattern, "eggspamsausagespam"))


pattern = r"pam"
match = re.search(pattern, "eggspamsausage")
if match:
   print(match.group())
   print(match.start())
   print(match.end())
   print(match.span())


str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

print(r"I am \r\a\w!") # remove r to see

# meta . for any
pattern = r"gr.y"

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "blue"):
   print("Match 3")

'''
The pattern "^gr.y$" means that the string should 
start with gr, then follow with any character, 
except a newline, and end with y.
'''
pattern = r"^gr.y$"

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "stingray"):
   print("Match 3")

# character classes:
pattern = r"[aeiou]"
'''
The pattern [aeiou] in the search function 
matches all strings that contain any one of 
the characters defined.
'''

if re.search(pattern, "grey"):
   print("Match 1")

if re.search(pattern, "qwertyuiop"):
   print("Match 2")

if re.search(pattern, "rhythm myths"):
   print("Match 3")

pattern = r"[A-Z][A-Z][0-9]"
'''
The pattern in the example above matches 
strings that contain two alphabetic uppercase 
letters followed by a digit.
'''
if re.search(pattern, "LS8"):
   print("Match 1")

if re.search(pattern, "E3"):
   print("Match 2")

if re.search(pattern, "1ab"):
   print("Match 3")

'''
Place a ^ at the start of a character class to invert it.
This causes it to match any character other than the ones included.
Other metacharacters such as $ and ., have no meaning within character classes.
The metacharacter ^ has no meaning unless it is the first character in a class.
'''
pattern = r"[^A-Z]"
'''
The pattern [^A-Z] excludes uppercase strings.
Note, that the ^ should be inside the brackets to invert the character class.
'''

if re.search(pattern, "this is all quiet"):
   print("Match 1")

if re.search(pattern, "AbCdEfG123"):
   print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
   print("Match 3")

'''
The metacharacter * means "zero or more repetitions of the previous thing". It tries to match as many repetitions as possible. The "previous thing" can be a single character, a class, or a group of characters in parentheses.
'''
pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")

'''
The example above matches strings that start with "egg" and follow with zero or more "spam"s.
'''

# () means a group
# + one or more repetitions
# pattern = r"g+"
# ? means "zero or one repetitions".
# pattern = r"ice(-)?cream"
#  {0,1} is the same thing as ?.
# Curly braces can be used to represent the number of repetitions between two numbers.
# {1,} same as +
# {0,} sameas *
# | means or red|blue: either red or blue

print("---------------")
pattern = r"9{1,3}$"

if re.match(pattern, "99"):
   print("Match 1")

if re.match(pattern, "999"):
   print("Match 2")

if re.match(pattern, "9999"):
   print("Match 3")


# '([^aeiou][aeiou][^aeiou])+'
# the above mean One or more repetitions of a non-vowel, a vowel and a non-vowel


pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
   print(match.group())
   print(match.group(0))
   print(match.group(1))
   print(match.group(2))
   print(match.groups())


"""
Two useful ones are named groups and non-capturing groups.
Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. They behave exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.
Non-capturing groups have the format (?:...). They are not accessible by the group method, so they can be added to an existing regular expression without breaking the numbering.
"""
pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.groups())


# Special Sequences
'''
One useful special sequence is a backslash and a number between 1 and 99, e.g., \1 or \17. This matches the expression of the group of that number.
Note, that "(.+) \1" is not the same as "(.+) (.+)", because \1 refers to the first group's subexpression, which is the matched expression itself, and not the regex pattern.
'''
# any thing followed by the same thing
pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
   print ("Match 1")

match = re.match(pattern, "?! ?!")
if match:
   print ("Match 2")    

match = re.match(pattern, "abc cde")
if match:
   print ("Match 3")

'''
More useful special sequences are \d, \s, and \w.
These match digits, whitespace, and word characters respectively.
In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
In Unicode mode they match certain other characters, as well. For instance, \w matches letters with accents.
Versions of these special sequences with upper case letters - \D, \S, and \W - mean the opposite to the lower-case versions. For instance, \D matches anything that isn't a digit.
'''
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


# "123!456!" == [1-6!] == (\d*\W)+


'''
Additional special sequences are \A, \Z, and \b.
The sequences \A and \Z match the beginning and end of a string, respectively.
The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. Informally, it represents the boundary between words.
The sequence \B matches the empty string anywhere else.
'''
# \b(cat)\b" basically matches the word "cat" surrounded by word boundaries
pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
   print ("Match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
   print ("Match 2")

match = re.search(pattern, "We scattered.")
if match:
   print ("Match 3")

# Which pattern would match 'SPAM!' in a search?
# \AS...\b.\Z


# Email Extraction
# dot dollowed by \ to treat it like character
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

'''
The regex above says that the string should contain a word (with dots and dashes allowed), followed by the @ sign, then another similar word, then a dot and another word.
Our regex contains three groups:
1 - first part of the email address.
2 - domain name without the suffix.
3 - the domain suffix.
'''
str = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
   print(match.group())

'''
In case the string contains multiple email addresses, we could use the re.findall method instead of re.search, to extract all email addresses.
'''

# "(4{5,6})\1" means 10 or 12 fours












































































