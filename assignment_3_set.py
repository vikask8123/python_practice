#set assignment

"""1. Write a program to create an empty set."""
s = set()

print(s)
print(type(s))

"""2. Create a set from a list of elements."""
l = [111,222,333,444,111,444,333,777]

s = set(l)
print("List:",l)
print("Set:",s)

"""3. Write a program, to create new which will contain common elements in two 
different sets."""

set_1 = {15,9,10,56,22,58,4,6,3}
set_2 = {9,4,5,36,47,26,10,45,87}

print("set one:",set_1)
print("set two:",set_2)
print("Common elements in both sets:",set_1&set_2)
print("Common elements using intersections of sets:",set_1.intersection(set_2))


"""4. Write a program to get unique items from two sets."""

set_1 = {15,9,10,56,22,58,4,6,3}
set_2 = {9,4,5,36,47,26,10,45,87}

print("set_1:",set_1)
print("set_2:",set_2)

print("Unique items from two sets:",set_1.symmetric_difference(set_2))
print("Unique items using caret sign:",set_1^set_2)

"""5. Update the first set with items that don’t exist in the second set."""

set_1 = {15,9,10,56,22,58,4,6,3}
set_2 = {9,4,5,36,47,26,10,45,87}

print("set_1:",set_1)
print("set_2:",set_2)

set_1.difference_update(set_2)

print("Output set oen:",set_1)

"""6. Write a program to return a set of elements present in set a or b, but not both."""

set_1 = {15,9,10,56,22,58,5,4,9}
set_2 = {9,4,5,36,47,26,1,4,87}

print("set_1:",set_1)
print("set_2:",set_2)

print("Output one:",set_1.symmetric_difference(set_2))
print("Output two:",set_1^set_2)

"""7. Write a program to check if two sets have any elements in common. If yes, 
display the common elements."""

set_1 = {15,9,10,56,22,58,5,4,9}
set_2 = {9,4,5,36,47,26,1,4,87}

print("set_1:",set_1)
print("set_2:",set_2)

print("Common elements in both sets:",set_1&set_2)

"""8. Write a program to remove items from set1 that are not common to both set1 
and set2."""

set_1 = {15,9,10,56,22,58,5,4,9}
set_2 = {9,4,5,36,47,26,1,4,87}

print("set_1:",set_1)
print("set_2:",set_2)

set_1.symmetric_difference(set_2)

print("Update set one:",set_1)

"""9. Write a program to create set of even numbers only."""
s = set(range(0,21,2))

print("Set of even numbers:",s)

"""10. Write a program to get size of set."""
from sys import getsizeof
s = set(range(0,21,2))

print("set is:",s)

print("Set size:",getsizeof(s))

"""11. Write a program to convert set into tuple and tuple into set."""

s = set(range(1,11))
print("set is:",s)

t = tuple(range(21,31))
print("Tuple is:",t)

s_t = tuple(s)
print("Set in to tuple:",s_t)

t_s = set(t)
print("Tuple in to set:",t_s)






