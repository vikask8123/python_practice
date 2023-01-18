num_list = [1,2,3]
print(len(num_list))

num_list = [1,2,3]
print(num_list)

num_list.append(111)
print("updated 1:",num_list)

n_list = [1,2,3,1,2,3,111]
print(n_list.index(111))

print(n_list.count(3))

n_list.append(100)
print(n_list)

n_list.insert(0,999)
print(n_list)

l1 = [1,2,3]
l2 = [111,222,333]
l1.extend(l2)
print(l1)

l1.remove(333)
print(l1)

l1.pop(2)
print(l1)

l1.clear()
print(l1)

del(l1)

print(l1)
