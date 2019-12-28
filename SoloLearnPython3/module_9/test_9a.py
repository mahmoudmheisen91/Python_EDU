# Zen of Python
import this

'''
There are 20 principles in the Zen of Python, but only 19 lines of text.
The 20th principle is a matter of opinion, but our interpretation is that the blank line means "Use whitespace"
'''

# Python Enhancement Proposals (PEP)
'''
Python Enhancement Proposals (PEP) are suggestions for improvements to the language, made by experienced Python developers.
PEP 8 is a style guide on the subject of writing readable code. It contains a number of guidelines in reference to variable names, which are summarized here:
- modules should have short, all-lowercase names;
- class names should be in the CapWords style;
- most variables and function names should be lowercase_with_underscores;
- constants (variables that never change value) should be CAPS_WITH_UNDERSCORES;
- names that would clash with Python keywords (such as 'class' or 'if') should have a trailing underscore.

PEP 8 also recommends using spaces around operators and after commas to increase readability.

Other PEP 8 suggestions include the following:
- lines shouldn't be longer than 80 characters;
- 'from module import *' should be avoided;
- there should only be one statement per line.

It also suggests that you use spaces, rather than tabs, to indent. However, to some extent, this is a matter of personal preference. If you use spaces, only use 4 per line. It's more important to choose one and stick to it.

The most important advice in the PEP is to ignore it when it makes sense to do so. Don't bother with following PEP suggestions when it would cause your code to be less readable; inconsistent with the surrounding code; or not backwards compatible.
However, by and large, following PEP 8 will greatly enhance the quality of your code.
Some other notable PEPs that cover code style:
PEP 20: The Zen of Python
PEP 257: Style Conventions for Docstrings

'''

'''
The parameter *args must come after the named parameters to a function.
The name args is just a convention; you can choose to use another.
'''
def function(named_arg, *args):
   print(named_arg)
   print(args)

function(1, 2, 3, 4, 5)


'''
In case the argument is passed in, the default value is ignored.
If the argument is not passed in, the default value is used.

These must come after named parameters without a default value.
'''
def function2(x, y, food="spam"):
   print(food)

function2(1, 2)
function2(3, 4, "egg")

'''
**kwargs (standing for keyword arguments) allows you to handle named arguments that you have not defined in advance.
The keyword arguments return a dictionary in which the keys are the argument names, and the values are the argument values.
'''
def my_func(x, y=7, *args, **kwargs):
   print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)


# Tuple Unpacking
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

# swap variables by doing a, b = b, a

# A variable that is prefaced with an asterisk (*) takes all values from the iterable that are left over from the other variables.
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

# Ternary Operator
a = 7
b = 1 if a >= 5 else 42
print(b)


'''
With the for or while loop, the code within it is 
called if the loop finishes normally (when a 
break statement does not cause an exit from 
the loop).
'''
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

'''
The else statement can also be used with 
try/except statements.
In this case, the code within it is 
only executed if no error occurs in the 
try statement.
'''

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

"""
Most Python code is either a module to be imported, or a script that does something.
However, sometimes it is useful to make a file that can be both imported as a module and run as a script.
To do this, place script code inside if __name__ == "__main__".
This ensures that it won't be run if the file is imported.
"""
def function4():
   print("This is a module function")

if __name__=="__main__":
   print("This is a script")

'''
When the Python interpreter reads a source file, it executes all of the code it finds in the file. Before executing the code, it defines a few special variables.
For example, if the Python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name.
'''

if __name__== "__main__":
   print("Hi") # script
else:
   print("Welcome") # module

'''
For scraping data from websites, 
the library BeautifulSoup is very useful, 
and leads to better results than building 
your own scraper with regular expressions.
'''

'''
In Python, the term packaging refers to putting modules you have written in a standard format, so that other programmers can install and use them with ease.
This involves use of the modules setuptools and distutils.
The first step in packaging is to organize existing files correctly. Place all of the files you want to put in a library in the same parent directory. This directory should also contain a file called __init__.py, which can be blank but must be present in the directory.
This directory goes into another directory containing the readme and license, as well as an important file called setup.py.

SoloLearn/
   LICENSE.txt
   README.txt
   setup.py
   sololearn/
      __init__.py
      sololearn.py
      sololearn2.py

The next step in packaging is to write the setup.py file.
This contains information necessary to assemble the package so it can be uploaded to PyPI and installed with pip (name, version, etc.).
Example of a setup.py file:

from distutils.core import setup

setup(
   name='SoloLearn', 
   version='0.1dev',
   packages=['sololearn',],
   license='MIT', 
   long_description=open('README.txt').read(),
)

After creating the setup.py file, upload it to PyPI, or use the command line to create a binary distribution (an executable installer).
To build a source distribution, use the command line to navigate to the directory containing setup.py, and run the command python setup.py sdist.
Run python setup.py bdist or, for Windows, python setup.py bdist_wininst to build a binary distribution.
Use python setup.py register, followed by python setup.py sdist upload to upload a package.
Finally, install a package with python setup.py install.

The previous lesson covered packaging modules for use by other Python programmers. However, many computer users who are not programmers do not have Python installed. Therefore, it is useful to package scripts as executable files for the relevant platform, such as the Windows or Mac operating systems. This is not necessary for Linux, as most Linux users do have Python installed, and are able to run scripts as they are.

For Windows, many tools are available for converting scripts to executables. For example, py2exe, can be used to package a Python script, along with the libraries it requires, into a single executable.
PyInstaller and cx_Freeze serve the same purpose.
For Macs, use py2app, PyInstaller or cx_Freeze.

'''













