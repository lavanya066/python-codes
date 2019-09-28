
m=[]
b=3
for i in range(b):
    a=[]
    for j in range(b):
        l=int(input('enter'))
        a.append(l)
     
    m.append(a)
print("*******")
a=[]
for i in range(b):
    l=int(input('enter'))
    a.append(l)
h=[2,3,4]
m.append(a)
b=b+1
count=0
l1=len(m)
print(l1)
f=[]

for i in range(l1):
  
    for j in range(i+1,l1):
        #for k in range (len(m[0])):
        if(m[i]==m[j]):
            f.append(m[i])
            
            l1=l1-1
            count=count+1
            print(m[i])
lo=len(f)
for i in range(lo):
    m.remove(f[i])

print(m)
print(l1)
print("********")
print(count)

