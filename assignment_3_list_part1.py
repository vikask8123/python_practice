"""1. Create a list of only even numbers."""

even_list = list(range(0,50,2))
print("Even number list: ",even_list)

"""2. Create one list of 1 to 10 numbers and create new list which contain square of the 
numbers from this number list."""

num_list = list(range(1,11))
print("Number list:",num_list)

sq_list = []

for i in num_list:
    sq_list.append(i**2)
    
print("square list: ",sq_list)

"""3. Take three input numbers from the user and create list from those numbers.
"""

num1,num2,num3 = input("enter three numbers: ").split()
num_list = []

num_list.append(int(num1))
num_list.append(int(num2))
num_list.append(int(num3))

print("Update number list is: ",num_list)

"""4. Take one list of numbers and do sum of all numbers in that list without using sum 
function."""

num_list = list(range(1,6))
print("Number list",num_list)

total = 0
for num in num_list:
    total += num
    
print("Final total list is:",total)

"""5. list_one = [1,2,3,4], list_two =[1,2,3,4], check that these two lists content is same of 
not"""
list_one = [1,2,3,4]
list_two = [1,2,3,4,5]
print(list_one==list_two)

"""6. list_one = [1,2,3,4], list_two =[1,2,3,4], check that these two lists """

list_one = [1,2,3,4]
list_two = [1,2,3,4]

print("list one address:",id(list_one))
print("list two address:",id(list_two))

print(list_one is not list_two)

"""7. list1 = [100,200,100,400,500,300], reverse this list."""

list1 = [100,200,100,400,500,300]
print("Original lsit:",list1)

list1.reverse()

print("After reversal:",list1)

"""8. Reverse above list without using reverse function"""

list1 = [100,200,100,400,500,300]
print("Orginal list:",list1)
# [100,200,100,400,500,300] 5,4,3,2,1,0
op_list =[]
len_list = len(list1)
for i in range(1,len_list+1):
    op_list.append(list1[len_list-i])
    print(op_list)
    
print("Final output list is:",op_list)

"""9. Reverse the above lists using slicing."""
list1 = [100,200,100,400,500,300]
print("orginal list:",list1)
op_list = list1[::-1]
print("Reverse list:",op_list)

"""10. Concatenate two list index wise,
Eg.l1 = [‘A’,’B’,’C’]
l2 = [‘X’,’Y,’Z’]
o/p: [‘AX’,’BY’,’CZ’]"""

l1 = ['A','B','C']
l2 = ['X','Y','Z']
op_list = []
for i in range(len(l1)):
    op_list.append(l1[i]+l2[i])
    
print("Final output list is:",op_list)

"""11. Create one list of numbers from 1 to 10 and extract only last 5 numbers from that 
list."""
num_list = list(range(1,11))
print("Number list is:",num_list)

print(num_list[-5:])

"""12. Take a list of names and convert those all names into Upper case words."""

name_list = ["vikas","vinay","vijay","naagu"]
print("Orginal name list is:",name_list)
op_list = []
for name in name_list:
    op_list.append(name.upper())
    
print("Final output list:",op_list)

"""13. Take list of names and count number of characters in each name and print on the 
console, name and its length."""

name_list = ["venu","sudarshan","bunny","ragu"]

for name in name_list:
    print(f" name is {name} and length is {len(name)}")
    
"""14. Create one list of elements and take specific element and position of element from 
user and add that element at that position"""

list_num = list(range(1,11))

print("Number list is:",list_num)

num = int(input("Enter anumber to insert in list:"))

position = int(input("Enter positions to insert element:"))

list_num.insert(position,num)
print("Update list:",list_num)

"""15. Take list of numbers and print on the console element and number of occurrences of 
that element in that list."""


num_list = [1,2,3,4,5,12,3,1,2,3,4,1,9,11,12]
print("Original number lsit:",num_list)

num_set = set(num_list)

print("final number list is:",num_set)

for num in num_set:
    print("number is:",num,"count is:",num_list.count(num))

"""16. Check the start and end element of the lists are same or not."""
number_list = [10,2,3,4,1,2,3,5,9,10]
print(len(number_list))
print(number_list[0]==number_list[len(number_list)-1])

"""17. Take the list of strings and sort in both ascending and descending order"""

string_list = ["Ant","cat","zoom","Snoop","Kiran","fathima","Anoop"]

print("Original list:",string_list)

string_list.sort(reverse=True)
print("sorted list:",string_list)


"""18. Take a number list and calculate sum and average of list elements."""

num_list = list(range(1,11))
print("Number list is:",num_list)

num_sum = 0
for num in num_list:
    num_sum += num
    
avg = num_sum/len(num_list)
print(f"Sum is {num_sum} and average is {avg}")

"""19. Take a number list and count even and odd numbers in that list."""

num_list = list(range(0,111))

print(num_list)
even_count = 0
odd_count = 0
for num in num_list:
    if num%2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
print("Even number count:",even_count)
print("odd number count:",odd_count)


"""20. Get only unique elements from the list."""

num_list = [1,2,3,1,2,3,1,23,2,4,5,64,5,55,55,4,5]

print("Original list:",num_list)

unq_elem_list = list(set(num_list))

print("Unique elements list is:",unq_elem_list)


"""22. Take two lists with same number of elements and subtract elements from one list 
from other list element and create new list for that subtraction result."""

list_one = [99,88,66,44,11,55]
list_two = [4,6,8,7,9,2]
print("List one:",list_one)
print("list two:",list_two)

op_list = []
for i in range(len(list_one)):
    op_list.append(list_one[i]-list_two[i])
    
print("Result list is:",op_list)

"""22. Take one list elements and create two separate lists those contain odd numbers and 
even numbers separately."""

num_list = list(range(0,111))
print("Orginal list:",num_list)

even_list = []
odd_list = []
for number in num_list:
    if number%2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)
        
print("Even numbers list:",even_list)
print("Odd number list:",odd_list)

"""23. Take a list of numbers in the string format, convert those numbers into integer 
format and get sum of all those list elements."""

list_num = ["1","3","8","18","4","9"]
print("Original list:",list_num)

total = 0
for num in list_num:
    total += int(num)
    
print("Additon of number:",total)

 
