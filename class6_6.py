class student:
    def __init__(self):
        print("constructor called")
        print("inside constructor: ",id(self))
    def display(self):
        print("Display method called")
        print("inside display: ",id(self))
s1 = student()
s1.display()

s2 = student()
s2.display()

