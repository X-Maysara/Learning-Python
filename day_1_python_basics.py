# I want to print hello world
print("Hello world!")

# Data types
print("Mysra") # This is string data type you can write it in 'str', "str", '''str''', """str""" 
print(type("Mysra"))

print(18) # This is integer data type is from negative infinte to postive infinte
print(type(18))

print(1.0901) # This is float data type is every fracture
print(type(1.0901))

print(True) # This Flase or True which is 1 or 0 False is every thing empty and its sympoled by  0 and True is the oppoiste and is sympoled by 1
print(type(True))

# f-string: It can print data types as string
print(f"`{18}` is integer data type")

print(f"`{1.0901}` is float data type")

print(f"`{True}` is bool data type")

# Convert to another data type
print(f"`{18}` is {type(18)} convert to {type(str(18))}")

print(f"`{18}` is {type(18)} convert to {type(float(18))}")

print(f"`{18}` is {type(18)} convert to {type(bool(18))}")


# Mathmatice opertion
"""
Mathmatice opertion order:
	The first one to be opereted is `**`  and folowed by `*` `/` in the same level and `=` `-` in the same level
	 And you can skip the order by adding ()
"""
print(f"{1} + {6} = {1 + 6}") # Plus opertion

print(f"{9} - {18} = {9 - 18}") # Minus opertion

print(f"{6} * {24} = {6 * 24}") # Multiply opertion

print(f"{89} / {9} = {89 / 9}") # divid opertion

print(f"{23} ** {2} = {23 ** 2}") # power opertion

print(f"{(2 + 2) * 89 * 70 / 60} ")

print(2 ** (2 + 7))

print((3 * 5) ** ((4 - 2) / 16))

print((188 ** 200) / ((70 - 27) ** 2938))
