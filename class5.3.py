#lambda

sum_numbers = lambda a,b:a+b
print(sum_numbers(10,20))
square_number = lambda a:a*a
print(square_number(20))

#filters

def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l=[0,5,10,15,20,25,30]
ll=list(filter(isEven,l))
print(ll)

#l=[0,5,10,15,20,25,30]
#l3=list(filter(lambda x:x%2==0,l))
#print(l3)
#l2=list(filter(lambda x:x%2!=0,l))
#print(l2)

#without lambda
l=[1,2,3,4,5]
def double_it(x):
    return 2*x
ll=list(map(double_it,l))
print(ll)

l2=[1,2,3,4,5]
l3=list(map(lambda x:2*x,1))
print(l3)
