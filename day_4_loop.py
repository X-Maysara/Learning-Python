# For loop
for i in range(10):
	print(i)

print(f"Final i = {i}")


for char in "abcde":
	print(char)

num = [1, 2, 3, 4, 5, ]

for i in num:
	print(i)


for i in range(11):
	if i % 2 == 0:
		print(f"This number is an even number: {i}")
	else:
		print(f"This number is an odd number: {i}")


dict_1 = {
'name' : 'mysra',
'age': 12,
"list": [1, 2, 3, 4, 5]
}

for key,value in dict_1.items():
	print(f"key: {key} - value: {value}")

for num in range(10):
	print(num)
else:
	print("For loop is over")


# While loop
num = 0
while num <= 10:
	print(num)

	num = num + 1

num = 10
while num >= 0:
	print(num)

	num -= 1


num = 0
while num <= 10:
	print(num)

	num = num + 1
else:
	print("The while loop is over")
