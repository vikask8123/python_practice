l1=[1,2,3,4]
l2=[2,3,4,5]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)

#reduce function
from functools import reduce
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result)

