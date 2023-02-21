#Tuple
"""1. Create tuple of numbers 1 to 10."""

num_tuple = tuple(range(1,11))

print("Tuple is:",num_tuple)

"""2. Create single value tuple.
2. Create single value tuple."""

single_value_tp = (8,)
print(type(single_value_tp))
print("Single value tuple is:",single_value_tp)

"""3. Create one number element tuple and square all the elements in that tuple and 
store in new list."""

one_tuple = tuple(range(1,15))
print("Old tuple is:",one_tuple)
new_list_tp = []

for new in one_tuple:
    new_list_tp.append(new**2)

print("New list is:",new_list_tp)

"""4. Write a Python program to create a tuple."""

num = (1,2,3,4,'a','b',7,True)
print("num:",num)

"""5. Write a Python program to create a tuple with different data types."""

t1 = (1,2,3,4,'a','b',7,True,'pune','bangalore')
print("t1:",t1)    
    
"""6. Write a Python program to create a tuple of numbers and print 2nd item"""

t2 = tuple(range(1,11))
print("t2:",t2)

print(t1[1])

"""7. Write a Python program to unpack a tuple into several variables.
"""
#packing
a = 50
b = 20
c = 80
t = a,b,c
print(type(t))
print(t)

x,y,z = t
#unpacking
print(x,y,z)
print("x:",x)
print("y:",y)
print("z:",z)

"""8. Write a Python program to add an item to a tuple."""
#b1 = (1,2,3,4,5,6)
#print(b1)

#b1[0] = 100  (tuples cannot take add beacuse tuple is immutable )
#print

"""9. Write a Python program to convert a list to a tuple.
"""

num_list = list(range(1,9))

print("List is:",num_list)

num_tuple = tuple(num_list)
print("Tuple is:",num_tuple)

"""10. Write a Python program to find the length of a tuple without using len function."""

t1 = tuple(range(1,9))
print("t1:",t1)

c = 0
for t in t1:
    c += 1
    
print("Length of tuple:",c)

"""11. Write a Python program to reverse a tuple"""

a1 = (1,2,3,4,5,6,7,8)
print("orginal tuple:",a1)
op_tuple = tuple(reversed(a1))
print("Output tuple:",op_tuple)

"""12. Write a Python program to convert a list of tuples into a dictionary."""

list_one = [("a",100),("b",200),("c",300)]
print("List one is:",list_one)

dict_one = dict(list_one)

print("Dictionary:",dict_one)

"""13. Write a Python program to calculate the product, multiplying all the numbers in a 
given tuple."""

num_tuple = tuple(range(1,11))

print("Number tuple is:",num_tuple)

m = 1
for num in num_tuple:
    m *= num
print("Multiplication of all numbers is:",m)

"""14. Write a Python program to calculate the average value of the numbers in a given 
tuple"""

num_tuple = tuple(range(1,11))
print("Original tuple is:",num_tuple)

s = 0
for num in num_tuple:
    s += num
    
print("Sum is:",s)

avg = s/len(num_tuple)

print("Average is:",avg)

"""15. Write a Python program to convert a tuple of string values to a tuple of integer 
values"""

string_tuple_one = ("1","2","3","4","5")

print("String num tuple:",string_tuple_one)

num_list = []
for num in string_tuple_one:
    num_list.append(int(num))

print("Number list is:",num_list)

num_tuple = tuple(num_list)

print("Final output tuple:",num_tuple)


"""16. Write a Python program to convert a given list of tuples to a list of lists."""

list_of_tup = [("A","a"),("B","b"),("C","c")]
print("List of tuple is:",list_of_tup)

op_list = []

for t in list_of_tup:
    op_list.append(list(t))
    
print("Final output list is:",op_list)

"""17. Write a python program to get size of tuple."""

from sys import getsizeof

t = tuple(range(1,15))

print("Tuple is:",t)

print("Size of tuple is:",getsizeof(t))

"""18. Create one and list and one tuple with same elements and compare their sizes."""

from sys import getsizeof

num_list = list(range(1,11))
print("Number list:",num_list)

num_tuple = tuple(range(1,11))

print("Number tuples:",num_tuple)

print("Size of list:",getsizeof(num_list))
print("Size of list:",getsizeof(num_tuple))

"""19. Get count a particular element in tuple."""

num_tuple = (1,2,1,2,3,4,4,6,5,6,7,3)
print("Original tuple:",num_tuple)
s = set(num_tuple)
for n in s:
    print("Number is:",n,"count is:",num_tuple.count(n))
    
"""20. Write a Python program to get the 4th element and 4th element from last of a tuple"""

t = tuple(range(1,11))
print("Tuple is:",t)

print("4TH element from first part:",t[3])

print("4th element for last part:",t[-4])







                  
















    

 




    




