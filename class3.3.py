#this is simple function
def print_line():
    print("hello world")

#print("out of the function")
print_line()

print("""hello world,
      welcome to bangalore""")

a = 10
b = 20
t = a+b
print(t)

name = "ram"
age = 22
print(name,age)

print("name is:",name)
print("age is:",age)

print("name is:",name,"age is:",age)

    
print("HI %s your age is %d"%(name,age))

name = "ram"
age = 22
print("hey {} your age is {}".format(name,age))

print("hey {1} your age is {0}".format(name,age))

print("hey {st_name} your age is {st_age}".format(st_name="marry",st_age=20))

print("hey {0} your age is {1}".format(name,age))

name = "ram"
age = 22
print(name,age)
print(id(name))
print(id(age))
print(type(name))
print(type(age))

print("""hello world,
welcome to india""")

def add_fun():
    a = 30
    b = 20
    t = a+b
    print(t)

add_fun()

name = "ram"
age = 22
print("hi %s your age is %i"%(name,age))
print("hi",name,"your age is",age)

