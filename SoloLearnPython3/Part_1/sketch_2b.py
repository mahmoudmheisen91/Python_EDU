# simple calculator:
while True:
	print("Options:")
	print("Enter 'add' to add two numbers")
	print("Enter 'sub' to subtract two numbers")
	print("Enter 'mul' to multiply two numbers")
	print("Enter 'div' to divide two numbers")
	print("Enter 'q' to end the program")
	user_input = input(": ")

	if user_input == "q":
		break
	elif user_input not in ["add", "sub", "mul", "div"]:
		print("Unknown operation")
	else:
		num1 = float(input("enter num 1: "))
		num2 = float(input("enter num 2: "))
		if user_input == "add":
			print(f"result: {num1 + num2}")
		elif user_input == "sub":
			print(f"result: {num1 - num2}")
		elif user_input == "mul":
			print(f"result: {num1 * num2}")
		elif user_input == "div":
			print(f"result: {num1 / num2}")

