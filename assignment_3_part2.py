"""13. Ask user to enter number from 0 to 255 and print on the console its corresponding 
character."""
number = int(input("Enter a number 0 to 255:"))

print(chr(number))

"""14. Get word count , from paragraph."""

para = """
welcome to my city Banglore city is very beautiful,visit banglore in winter.
"""
print(para)
para_lower = para.lower()
print(para_lower)
print(para_lower.count("banglore"))

"""15. Take input string from user, while entering string if user gives spaces at starting or 
ending of the string, remove those spaces and print string on the console."""

string = input("Enter string: ").strip()
print(string)

"""16. Reverse the entered 4-digit number. Eg. input is 1804, o/p should be: 4081."""

number = int(input("Enter a number: "))
print("original number:",number)
str_num = str(number)
rev_num = str_num[::-1]
print(rev_num)
print(type(rev_num))

int_num = int(rev_num)
print(type(int_num))
"""or"""
def reverse_number(num):
    return int(str(num)[::-1])
num = 1804
print(reverse_number(num))


"""17. Take two string and add alphabets alternatively and form single string.eg.st1 = “BAT” 
,st2=”GIT”, then output should be: BGAITT."""

st1 = "BAT"
st2 = "GIT"
for i in range(len(st1)):
    print(st1[i]+st2[i],sep="",end="")


"""18. Count number of vowels in the string."""

string = input("enter a string:")

v_list = ["a","e","i","o","u"]

v_set = set()

for s in string:
    if s in v_list:
        v_set.add(s)
        
print("Vowels is string are: ",v_set)
print("count of vowels in string is: ",len(v_set))

"""19. Remove any special symbol, numbers from the list, keep only alphabets"""

string = input("enter string: ")
char_list = []
for s in string:
    if s.isalpha():
        char_list.append(s)
        
print(char_list)

new_str = "".join(char_list)

print(new_str)

"""20. Take two input strings from the user and check are those strings same or not."""

st1 = input("enter first string:")
st2 = input("enter second string:")

#print(st1==st2)
if st1==st2:
    print("both strings are same")
else:
    print("string are not same")


"""21. Write a program to get size of string."""    

import sys
string = input("enter a string: ")
print("size of string in bytes is: ",sys.getsizeof(string))
