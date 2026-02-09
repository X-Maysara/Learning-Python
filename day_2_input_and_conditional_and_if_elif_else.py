# accepting input from the user
anything = input("Enter anything: ")

# This print print what the user enterd and input function data type 
print(f"You have Enterd: {anything}\nThe data type of input function is: {type(anything)}")

num = input("enter any number: ")
print(f"You have enterd {num}\nThe data type of input function is: {type(num)}\nI turned it into Int data type: {int(num)} data typeis : {type(int(num))}")

float_var = input("enter any fracture: ")
print(f"You have enterd{float_var}\nThe data type of input function is: {type(float_var)}\nI turned it into float data type: {float(float_var)} data typeis : {type(float(float_var))}")

bool_var = input("enter anything: ")
print(f"You have enterd {bool_var}\nThe data type of input function is: {type(bool_var)}\nI turned it into Int data type: {bool(bool_var)} data typeis : {type(bool(bool_var))}")

#  using Conditional

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
print(f"First number: {num_1}\nSecond number: {num_2}")

print(f"First number == Second number: {num_1 == num_2}")
print(f"First number != Second number: {num_1 != num_2}")
print(f"First number < Second number: {num_1 < num_2}")
print(f"First number <= Second number: {num_1 <= num_2}")
print(f"First number > Second number: {num_1 > num_2}")
print(f"First number >= Second number: {num_1 >= num_2}")


# And, Or, Not

# AND
print(f"True And True is: {True and True}")
print(f"True And False is: {True and False}")
print(f"False And False is: {False and False}")
print(f"False And True is: {False and True}")

# OR
print(f"True Or True is: {True or True}")
print(f"True Or False is: {True or False}")
print(f"False Or False is: {False or False}")
print(f"False Or True is: {False or True}")

# NOT
print(f"Not True is: {not True}")
print(f"Not False is: {not False}")



# OR 
print((num_1 == num_2) or (True))
print((num_1 != num_2) or (num_1 <= num_2))

# AND
print(num_1 == num_2 and True)
print((num_1 != num_2) and 0)

#NOT
print(not (num_1 == num_2))
print(not (num_1 != num_2))


user_input = input("Enter a number: ")

if user_input != "":
	if user_input.isdigit():
		number = int(user_input)
	else:
		print("This string doesnot containe a number")
		number = "alphapatical"
else:
	print("You have enterd an empty string")
	number = "empty"


if (number != "empty") and (number != "alphapatical"):
	if number % 2 == 0:
		print(f"You have enterd: {number}, and this number is even number")
	elif number % 2 == 1:
		print(f"You have enterd: {number}, and this is an odd number")
	else:
		print(f"You have enterd: {number}, bla bla")

elif number == "empty":
	print("This virable is empty")

elif number == "alphapatical":
	print("This virable contains letters it doesnot contain numbers ")

else:
	print("This virable it's not digit, empty and not alphapatical")
