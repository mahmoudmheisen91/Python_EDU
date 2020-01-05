# Try except:
try:
	print(10)
	print(3/0)
except ZeroDivisionError:
	print("error")
except (ZeroDivisionError, ValueError):
	print("two errors")
except:
	print("all")
finally:
	print("always run")
print(5*"-")

# Assertion:
print(0)
assert 1 == 1
print(1)
assert 2 == 2
print(2) 

try:
	assert 2 == 1 # Assertion error
except AssertionError:
	print("Assertion Error")
finally:
	num = 3 # Assertion Message
	#assert (num < 0), "num is +ve"
	
