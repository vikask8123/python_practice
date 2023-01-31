#set

s1 = set()
print(type(s1))
print(s1)

s2 = set(range(1,11))
print(s2)

s3 = {}
print(type(s3))
print(s3)

l = [1,2,3,4,1,2,4,5,6,1,100,2,1] #its delet duplicate values and gives unique values
s4 = set(l)
print(s4)

d ={1:"a",2:"b",3:"c"}
s5 = set(d)
print(s5)

s6 = set(d.values())
print(s6)

s7 = set(range(1,7))
print(s7)
s7.add(111)
print(s7)

for i in s7:
    print(i)

