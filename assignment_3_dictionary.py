"""1. Create an empty dictionary then add some key value pairs, like 
name,age,address..etc"""

name,age,address = input("Enter your name, age and address:").split()
user_data = {}

user_data["name"] = name
user_data["age"] = int(age)
user_data["address"] = address

print("Final dictionary is: ",user_data)

print("Your name is:",user_data["name"])
print("Your age is:",user_data["age"])
print("Your address is:",user_data["address"])

"""2. Take two lists of same size and make first list members as key and second list 
elements as values."""

key_list = ["a","b","c","d","e"]
value_list = [20,23,26,90,38]
print("key list:",key_list)
print("value list:",value_list)
d = {}
l = len(key_list)

for i in range(l):
    d[key_list[i]] = value_list[i]

print("Final Output Dictionary:",d)    

"""3. Take one lists of duplicate numbers, and make a dictionary which key is list element 
and value is number of occurrences of that element in that list."""

list_one = [1,2,3,4,5,1,2,6,5,4,8,1,10,22]
print("Number list:",list_one)
num_set = set(list_one)
print("Number set:",num_set)

num_dict = {}

for num in num_set:
    num_dict[num] = list_one.count(num)

print("Output dictionary is:",num_dict)

"""4. Write a Python script to add a key to a dictionary.
"""

user_dict = {"name":"Ram","age":22,"city":"bangalore"}
print("Dictionary is:",user_dict)

user_dict["salary"] = 30000

print("updated dictionary is:",user_dict)

"""5. Write a Python program to iterate over dictionaries using for loops."""

user_dict = {'name': 'Ram', 'age': 22, 'city': 'bangalore', 'salary': 30000}

for key,value in user_dict.items():
    print(key,value)

"""6. Write a program to sum values in that dictionary."""

num_dict = {"a":23,"b":45,"c":30}

result_sum = sum(num_dict.values())

print("sum is:",result_sum)

result_sum_f = 0
for val in num_dict.values():
    result_sum_f += val
print("sum using for loop is:",result_sum_f)

"""7. Write a Python program to sort a given dictionary by key."""
d = {"a":1,"x":2,"c":3,"s":4}
print("Orginal dictionary:",d)
k = dict(sorted(d.items()))
print("Final output dictionary:",k)

"""8. Write a Python program to sort a given dictionary by values."""

"""9. Write a Python program to get the maximum and minimum values of a dictionary."""

d = {"a":90,"b":100,"c":60,"d":4,"e":40}

print("Minimum value is: ",min(d))

print("Maximum vale is:",max(d))

"""10. Write a Python program to get total number of items in that dictionary."""

d = {"a":90,"b":10,"c":22,"t":4,"f":2}

print("Total number of items is:",len(d))

"""11. Write a Python program to replace values of dictionary with sum of key and value."""

num_dict = {1:22,2:22,3:33,4:44,5:55}
print("Original Dictionary:",num_dict)

for key,value in num_dict.items():
    num_dict[key] = key+value

print("Output Dictionary:",num_dict)

"""12. Write a Python program, take on list of words and create new dictionary its words 
are keys of that dictionary and values as length of the word."""

word_list = ["pune","bangaluru","delhi","mumbai","mysore"]
print("Original list is:",word_list)
word_len = {}

for word in word_list:
    word_len[word] = len(word)
    
print("Output dictionary:",word_len)

"""13. Write a Python program to invert key, value pairs in dictionary."""

v = {"name":"Pavan","age":21,"address":"Banagaluru","salary":100000}
print("Original dictionary:",v)
emty_dict = {}

for key,value in v.items():
    emty_dict[value] = key
    
print("emty dictionary updated is:",emty_dict)

"""14. Write a Python program, take one numbers list and create new dictionary its key is 
number and value is square of that number from numbers list."""

num_list = list(range(1,11))
print("Number list is:",num_list)

d_op = {}

for num in num_list:
    d_op[num] = num**2
    
print("output dictionary:",d_op)

"""15. Merge two dictionaries into one dictionary."""
d1 = {"a":1,"b":2,"c":3}
d2 = {"x":11,"y":22,"z":33}
print("d1:",d1)
print("d2:",d2)

for key,value in d2.items():
    d1[key] = value
    
print("Mearged dictionary:",d1)

"""16. Write a Python program to sum all the dictionary values without using sum function."""

d = {"a":34,"b":48,"c":55,"d":80,"e":100}
print("Original dictionary:",d)
s = 0
for val in d.values():
    s += val
    
print("Summation of all values:",s)

"""17. Write a Python program to transform a dictionary into a list of tuples.
"""

d = {"a":34,"b":48,"c":55,"d":80,"e":100}
print("Original dictionary:",d)
item_list = []

for item in d.items():
    item_list.append(item)

print("Output list is:",item_list)

"""18. Write a python program to find size of dictionary."""

from sys import getsizeof

d = {"a":34,"b":48,"c":55,"d":80,"e":100}

size_dict = getsizeof(d)

print("Size of dictionary in bytes:",size_dict)

"""19. Create dictionary with key value pairs and then change value of particular key."""

d = {"a":34,"b":48,"c":55,"d":80,"e":100}

print("Original Dictionary is:",d)

d["a"] = 111

print("Update Dictionary is:",d)

"""20. Write a program, user will enter its details like name, age ..etc , create one dictionary 
for that and display readable information on the console of that user."""

name,age,city = input("Enter name,age and city:").split()
d = {}
d["name"] = name
d["age"] = int(age)
d["city"] = city

print("Your Information is saved as follows")
print("Name is:",d["name"])
print("Age is:",d["age"])
print("City is:",d["city"])











