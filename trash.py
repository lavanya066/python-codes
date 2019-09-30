a=[]#this is to find the max sum of non adjecent elements
l=int(input('enter the limit'))
for i in range(l):
    b=int(input('enter'))
    a.append(b)
max=0
v=[]
k=[]

    
for i in range(len(a)):#seperating even and odd part of the elements
    if(i%2!=0):
        v.append(a[i])
    if(i%2==0):
        k.append(a[i])
p=len(k)
g=len(v)
if ((len(a))%2==0 and k[p-1]<a[len(a)-1]):#length of matrix is to be even else if we replace the number will not be adjecent
    k.remove(k[p-1])#remove and replace as the first and last place of the matrix will not be adjecent
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
    


        
