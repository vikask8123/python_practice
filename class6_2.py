f=open("besant_data.txt",'r')
lines=f.readlines()
for line in lines:
    print(line,end="\t")
f.close()


