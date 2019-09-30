a=[]
m=[]
b=3
for i in range(b):
    a=[]
    for j in range(b):
        l=input('enter')
        a.append(l)
    m.append(a)
a=[]
for i in m:
    if i not in a:
        a.append(i)
print (a)