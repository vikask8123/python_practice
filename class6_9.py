class employee:
    def __init__(self):
        self.eno=100
        self.ename="Tony"
        self.esal=10000
e = employee()
print(e.__dict__)

class test:
    def __init__(self):
        self.a=20
        self.b=10
    def m1(self):
        self.c=30
t=test()
t.m1()
t.d=40
print(t.__dict__)

class student:
    school_name = "SGVG"

    def __init__(self):
        self.a=100

    def disp(self):
        a = 200
        print("The value of a is: ",self.a)
        print("The value of a is: ",a)
        print("School name: ",self.school_name)
        
s = student()
s.disp()
print(s.__dict__)
print(student.__dict__)

class Test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        print(b)
        
t=Test()
t.m1()
t.m2()

#class method:


class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print("{}walk with {} legs...".format(name,cls,legs))
        
Animal.walk("Dog")
Animal.walk("cat")



        
        
