#using dict function

tuple_list = [(100,"a"),(200,"b"),(300,"c")]
new_d = dict(tuple_list)
print(new_d)

#how to remove elements from dictionary

d7 = {"name":"ram","age":22,"city":"pune","salary":1000}
print("orginal dictionary:",d7)

#how to get all key,values,items of the dictionary
print("all key:",d7.keys())
print("all values:",d7.values())
print("all items:",d7.items())



d7 = {"name":"ram","age":22,"city":"pune","salary":1000}
print(d7.pop("city")) #removed element city
print(d7)
#print(d7.pop("state")) 
print(d7.pop("state","st"))
#how to copy to another element
d8 = d7
print("new dict:",d8)

d9 = d7.copy()
print("d9 is:",d9)

d10 = {1:23,2:45}
print(d10.setdefault(1))
print(d10)
print(d10.setdefault(100,"x12"))
print(d10)

d11 = {"a":1,"b":2}
d12 = {"x":111,"y":222}
print(d11)
print(d12)

d11.update(d11)
print("update d12:",d11)
print("sum of all values of d11:",sum(d11.values()))
print(sorted(d11))
print(sorted(d11.values()))



