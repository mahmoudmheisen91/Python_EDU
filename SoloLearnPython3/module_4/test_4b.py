#r+ opens the file for both reading and writing
import os 
print(os.getcwd())

file = open("SoloLearnPython3/module_4/test_file.txt", "r+")
#print(file.read())
#file.close()

#print(file.read(16))
print("---------------")

#print(file.read(4))
print("---------------")

#print(file.read(4))
print("---------------")

#print(file.read())
#file.close()

#print(file.readlines())
#file.close()

#for line in file:
#    print(line)

#file.close() 

a = file.write("This has been written to a file")
print(a)
print(file.read())
file.close()
print("---------------")

try:
   f = open("SoloLearnPython3/module_4/test_file.txt")
   print(f.read())
finally:
   f.close()
print("---------------")

# automatic close
with open("SoloLearnPython3/module_4/test_file.txt") as f:
   print(f.read())



