"""
1.Display three strings 'name','is','james''as'name**is**james'.
"""
s1 = "Name"
s2 = "is"
s3 = "james"
print(s1,s2,s3)
print(s1,s2,s3,sep="**")

"""
2. Accept two numbers input from user, and do mathematical operations, (addition,
subtraction, multiplication, division, modulo division, floor division)."""

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
print("addition:",num1+num2)


print("subtraction:",num1-num2)
print("multiplication:",num1*num2)
print("division:",num1/num2)
print("modulo division:",num1%num2)
print("Floor division:",num1//num2)

"""
3. Convert decimal number into octal number using , format specifier in print function"""

number = 123

print("%o"%(number))

"""4. Display float number with two decimal places, using print function.
"""
number = 123.45678
print("%.2f"%(number))

"""5. Take three different strings from input and assign to three different variables and 
display on the console.
"""

str1,str2,str3 = input("Enter three different names:").split()
print("Name 1:",str1)
print("Name 2:",str2)
print("Name 3:",str3)

"""6. Take a input string and convert each character into upper case."""

name = input("Enter your name:").upper()
print("Name is:",name)

""""7. Take input string and calculate its length without using len function."""

city = input("Enter your city name:")
l = 0
for i in city:
    l +=1
print(f"Length of {city} is {l}")

"""8. Take input string and extract only even position characters."""

name = input("Enter your name:")
for i in range(0,len(name),2):
    print(name[i],end=" ")


"""9. Take circle radius input from user and calculate area of a circle."""

redius = float(input("Enter redius of a circle:"))
pi = 3.14
area = pi*redius**2
print(f"Area of circle with redius {redius} is {area}")

""""10. Reverse a string by its words."""
string = input("Enter a string:")
sp_str = string.split()
#print(sp_str)
sp_str.reverse()
#print(sp_str)
final_op = " ".join(sp_str)
print(final_op)

"""11. Take input string from user and check that is entered string is palindrome or not."""

string = input("Enter a string:")
rev_string = string[::-1]
print(string==rev_string)

if string == rev_string:
    print("string is palindrome")
else:
    print("string is not palindrome")

"""12. Take one input string and find ASCII value of each character and print on the console 
with that character."""

string = input("Enter a string:")
for s in string:
    print("char is:",s,"ASCII value is:",ord(s))

    
    

