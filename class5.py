i = 1
while i <=10:
    print(i)
    i += 1
#such loops infinite loops

#i = 0
#while True:
   # i = i+1
   # print(i)
   
#nestd loops   
#for i in range(4):
    #for j in range(4):
       # print("i=",1,"j=",j)

#break statement

for i in range(10):
    if i==7:
        print("processing is enough..plz break")
     #   continue & break
    print(i)
    
print("we are done with loop execution")

for i in range(10):
    if i%2==0:
        continue
    print(i)

    
cart = [10,20,30,40,50,1000]
for item in cart:
    if item>=500:
        print("we cannot process this order")
        break
    print(item)

else:print("congrats.....all items processed successfullu")


    
