# Files:
import os

f = open(os.getcwd()+"\\text_file_1.txt", "r+")
print(f.read())
f.close()
