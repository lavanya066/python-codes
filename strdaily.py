a=[]
b=[]
r=27
for i in range(1,27):
    a.append(i)
print(a)
c=ord('a')
for i in range(1,27):
    b.append(chr(c))
    c=c+1
print(b)
l=int(input('enter'))
count=0
while(l>0):
    m=l%10
    
    for i in a :
        if(m==i):
            print(b[i-1])
    l=int(l/10)
   
print(count)

  

