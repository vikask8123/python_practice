#dictionary:

d1 = {}
print(type(d1))
print(d1)

d2 = {"name":"ram","age":22}
print(d2)

d2["city"] = "bangalore"
print(d2)

d2["name"] = "john"
print(d2)

print(d2["age"])

d2["age1"] = 22
print(d2)

d3 = {"name":"ram","name":"john"}
print(d3)

d4 = {"a":101,"b":102,"c":103}
print(d4)
print(d4["b"])

#print(d4["d"]) #key is not found or error

print(d4.get("a",111))

print(d4.get("z",111))

d5 = {"name":"mary","age":19,"address":"delhi"}
for key,value in d5.items():
    print(f"key is {key} and value is {value}")

