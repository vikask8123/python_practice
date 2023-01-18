a = 22
print("a first ",id(a))

a = 100
print("a second ",id(a))

num_list = [1,2,3]
print("a first ",id(num_list))

num_list.append(100)
print("a second ",id(num_list))


city = "bengaluru"
print(city)
print(city[0])
print(city[6])
print(city[-9])
print(city[-3])
print(len(city))
