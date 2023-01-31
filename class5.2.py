#def add (a,b):
   # print(a+b)
#add(2,1)

def add (*args):
    print(type(args))
    print(args)
add(2,3,4)
add(1,2)
add(1)
add()

def sum_fun (*arg):
    total=0
    for number in arg:
        total=total+number
        print("the sum",total)
sum_fun()
sum_fun(10)
sum_fun(10,20)
sum_fun(10,20,30,40)

#using keyword argivments

def print_number (a,b):
    print(a)
    print(b)
print_number(a=55,b=100)

#using **kwargs

def print_num (**kwargs):
    print(type(kwargs))
    print(kwargs)
print_num(a=55)
print_num(a=55,b=100)
print_num(a=5,b=10,c=4)

def number_display(**kwargs):
    for k,v in kwargs.items():
        print(k,"=",v)
number_display(n1=10,n2=20,n3=30)
number_display(roll_no=100,name="tony",marks=70,subject="java")


#scope of variables

x = 100
def print_num():
    a = 200
    print(f"value of a is {a}")
    print(f"inside function x is {x}")
print_num()
#print_num(f"value of x is {x}")


#globa varibles
a=10
def print_number():
    print(a)
def display_number():
    print(a)
print_number()
display_number()

a = 100
def print_num():
    a = 200
    print(f"value of a is {a}")
print_num()
print(f"value of a outside of function {a}")

a = 100
def print_num():
    global a
    a = 200
    print(f"value of a is {a}")

def display_num():
    print(a)
print_num()
print(f"value of a outside of function {a}")





