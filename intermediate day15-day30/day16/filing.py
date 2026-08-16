f= open("data.txt","r")
data=f.read()
print(data)
print(type(data))


line1=f.readline()
print(line1)

f.close()