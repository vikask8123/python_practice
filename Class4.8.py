s = {1,2,3,4,5,6,7,8,9}
s.add(111)
print(s)

l = [1,2,3]
t = (111,222,333)
s = {888,999,777}
s1 = set()
s1.update(l,t,s)
print(s1)

#copy function

s = {1,2,3,4,5,6,7}
s1 = s.copy()
print(s)

#remove elements from set

s = {1,2,3,4,5,6,7,8,9}
print(s.pop())
print(s)

#removing specified element

s = {1,2,3,4,5,6,7,8,9}
s.remove(9)
print(s)
#
s = {1,2,3,4,5,6,7,8,9}
s.discard(111)
print(s)

#set clear
s = {1,2,3,7}
s.clear()
print(s)

#operators in python

a = 5
b = 2
print(a/b)
print(a%b)
print(a**2)

print("floor division:",5//2)
print("floor division: ",-5//2)

print("hello"+"world")
print(18*4)
print("a"*3)
print([1,2,3]*3)

a = 100
b = 50
print(a>b)
print(a>1000)

z = 100
print(z)
print(z==1000)
print(z!=1000)
print(z!=100)

#logical operaters
a = 10
print(a>2 and a>5)
print(a>100 and a>5)
print(a>100 or a>5)
print(a>100 or a>1000)

#using not operater

print(not(a>100 or a>1000))

a = 100
a+=10
print(a)








