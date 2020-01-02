# Logics:
x = True # must be capital

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
