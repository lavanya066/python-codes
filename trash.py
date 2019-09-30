a=[]
l=int(input('enter the limit'))
for i in range(l):
    b=int(input('enter'))
    a.append(b)
max=0
v=[]
k=[]

    
for i in range(len(a)):
    if(i%2!=0):
        v.append(a[i])
    if(i%2==0):
        k.append(a[i])
p=len(k)
g=len(v)
if ((len(a))%2==0 and k[p-1]<a[len(a)-1]):
    k.remove(k[p-1])
    k.append(a[len(a)-1])
if (v[0]<a[0]):
    v.remove(v[0])
    v.append(a[0])
s=0
sm=0
for i in k:
    s+=i
for i in v:
    sm+=i
if(sm>s):
    print(sm)
else:
    print(s)
    #print(sum)
    


        