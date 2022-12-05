f=open('demo1.txt','r')
print(f.seek(11))
#print(f.read(68))
for x in f:
    print(x)
f.close()
#print(f.readlines())#read only first line 
