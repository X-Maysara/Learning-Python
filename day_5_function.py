# Simple function 
def hello():
	print("Hello World!")

# Call function
hello()

print(hello())

func = hello()
print(func)

# Complex function
def adition_multiply(first_number=0, second_number=0):
	 return first_number * first_number + second_number * second_number

# Call functionb
num = adition_multiply()
print(num)

adition_multiply(second_number=12, first_number=25) 

print(adition_multiply(second_number=12, first_number=25))

result = adition_multiply(second_number=12, first_number=25) 
print(result)