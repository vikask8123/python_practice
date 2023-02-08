class student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def student_info(self):
        print("Name is: ",self.name)
        print("Roll number is: ",self.roll_no)
        print("Marks: ",self.marks)
s1 = student("Ram",101,95)
s1.student_info()
s2 = student("John",102,94)
s2.student_info()


        
