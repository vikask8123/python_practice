import keyword
keyword = keyword.kwlist
print(keyword)

list_num = list()
print(list_num)

print(type(list_num))

seq_list = list(range(1,11))
print(seq_list)

even_num_list = list(range(0,11,2))
print(even_num_list)

odd_num_list = list(range(1,11,2))
print(odd_num_list)

num_list = list(range(9))
print(num_list)

a = [1,2,"Tony",(4,5),3,4,[1,4]]
for i in a:
    print(i)

    print(a[2])

    print(a[3:6])
            
