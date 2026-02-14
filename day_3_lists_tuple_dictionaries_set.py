# List
nums = [1, 5, 7, 2, 0, 3, 11, 6, 12]
print(f"Numbers are: {nums}")

print(f"First item, use postive index: {nums[0]}")
print(f"Last item, use negative index: {nums[-1]}")
print(f"Midel item, use postive index: {nums[4]}")
print(f"Midel item, use negative index: {nums[-5]}")

print(sum(nums))
print(max(nums))
print(min(nums))
nums.sort()
print(nums)
nums.reverse()
print(nums)


names = ["Max", "Mysra", "Ben", "Loid", "Kai"]
print(f"Pupils names are: {names}")

print(f"First item, use postive index: {names[0]}")
print(f"Last item, use negative index: {names[-1]}")
print(f"Midel item, use postive index: {names[4]}")
print(f"Midel item, use negative index: {names[-3]}")

names.sort()
print(names)
names.reverse()
print(names)

random = [1, True, 1.0, "yuo", [1, 6, 9, "mysra"]]
print(f"Random data types: {random}")

print(f"Last item, use postive index: {random[4]}")
print(f"First item from last item, use postive index: {random[4][0]}")
print(f"Last item from last item, use postive index: {random[4][-1]}")
print(f"Last item from last item from last item, use postive index: {random[4][-1][-1]}")

print(f"Lengths of the list random is: {len(random)}")
random.append("Jay")
random.insert(0, ["my", True, False])
random.append(1)
random.append(1)
print(random.count(1))
print(random.index(1))
random.extend(nums)
random.extend(names)
random.pop()
print(random.pop())
random.remove(True)
del random[0]
print(random)
random.clear()
print(random)
																																			


# tuple
num_tuple = (1, 2, 3, 4, 5, 6, 1, 2, 0, 0, 1)
print(num_tuple)
print(len(num_tuple))
print(num_tuple.count(1))
print(num_tuple.index(1))
print(max(num_tuple))
print(min(num_tuple))
print(sum(num_tuple))

nmaes = ("Jhone", "Mysra", "Ben", "Loid")
print(names)
print(len(names))

random = (True, 12, "Mysra", [1, 2, 3, 4,], ("Numbers", "nums"))
print(random)
print(len(random))



# set

nums = {0, 1, 2, 3, 4, 5}
print(f"Numbers in this sets are: {nums}")

nums = {0, 0, 1, 5, 1,  2, 3, 4, 5}
print(f"Numbers in this sets are: {nums}")

names = {"Max", "Mysra", "Ben", "Loid"} 
print(f"Names in this set are: {names}")

nums.add(8)
print(nums)

nums.pop()
print(nums)
print(nums.pop())
																																																																																						
nums.remove(3)
print(nums)


# dictinoary

dict_1 = {
"name": "mysra",
"age" : 12,
"Last": "hghg"
}

print(dict_1)

print(dict_1["name"])
print(dict_1["age"])

dict_1["age"] = 16
print(dict_1)

dict_1["Max"] = 16
print(dict_1)

print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())

print(dict_1.pop("Last"))
print(dict_1)
print(dict_1.popitem())
print(dict_1)
print(dict_1.get("name"))
print(dict_1.get("my", False))

# Convert to list, tuple, dict, set
a = [0, 1, 2, 3, 4, 5]
b = (0, 1, 2, 3, 4, 5)
c = {0, 1, 2, 3, 4, 5}
d = {
	"name" : "Ben", 
	"age" : 10,
	"q" : 21 
}

a_tuple = tuple(a)
print(a_tuple)

b_list = list(b)
print(b_list)

a_set = set(a)
print(a_set)

dic_1 = dict([('on', 'po'), ('print', 'nums'), ('my', 'age')])
print(dict_1)
dict_2 = dict(name="mysra", age=12, nums=[1, 2, 3, 4, 5, ])
print(dict_2)
