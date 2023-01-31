#is'is not operators

l1 = [1,2,3,4]
l2 = [1,2,3,4]
print(l1 is l2)

print("l1:",id(l1))
print("l2:",id(l2))
print(l1 is not l2)
print(l1==l2)

a = 100
b = 200
print(a==b)

#in not in membership operater

print(4 in l1)
print(100 in l2)
print(111 not in l2)

#condition statement
#if statement

#weekdays = ["m","t","w","th","f"]
#day = input("enter day first char: ").upper()
#if day in weekdays:
    #print("yes i have class")
    
#else:
    #print("today is holiday")
#print("eod")    


#weekdays = ["m","t","w","th","f"]
#weekends = ["s","sa"]
#day = input("enter day first char: ").upper()
#if day is weekdays:
    #print("i have class")
    
#elif day in weekends:
    #print("holiday")
    
#else:
   # print("my personal holoday")

s = "bangalore"
for x in s:
    print(x)
    
    
