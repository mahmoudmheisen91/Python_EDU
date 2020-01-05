# Files:
import os

try:
	f = open(os.getcwd()+"\\text_file_1.txt", "r+")
	#print(f.read())
	#print(f.read(16))
	#print(f.readlines())
	#for line in f:
	#	print(line)
	a = f.write("testing...")
	print(a)
	#print(f.read())
finally:
	f.close()


# With - auto close:
with open(os.getcwd()+"\\text_file_1.txt", "r+") as f:
	print(f.read())

