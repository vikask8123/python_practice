#3 staticmethods

class CustomMath:
    @staticmethod
    def add(x,y):
        print("The sum: ",x+y)

    @staticmethod
    def average(x,y):
        print("The average: ",(x+y)/2))

CustomMath.add(10,20)
CustomMath.product(10,20)
CustomMath.average(10,20)
