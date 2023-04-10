from capitalize import capitalize


if capitalize("hello") != "Hello":
	raise Exception("Function does not work!")

if capitalize("") != "":
	raise Exception("Function does not work!")

print("All tests passed")
