#f = open("abc.txt","r")
#data = f.read()
#print("file data:",data)

f = open("abc.txt","w")
f.write("python")
f.close()

f = open("abc.txt","r")
data = f.read()
f.close()
