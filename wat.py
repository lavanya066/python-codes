a=1221
l=len(str(a))
x=a
o=[]
while(x!=0):
    d=int(x%10)
    o.append(d)
    x=int(x/10)
x=a
while(x>1):
    d=int(x%100)
    o.append(d)
    x=int(x/10)
x=a
while(x>1):
    d=int(x%100)
    o.append(d)
    x=int(x/100)
e=[]
y=[]
t=[]
for i in o:
    if(len(str(i))==1):
        print(i)
        e.append(i)
        print("****")
    if(len(str(i))==2):
        u=int(i%10)
        d=int(i/10)
        y=[]
        for j in o :
            
            if   len(str(j))==1:
                if (u==d):
                    print(j)
                    #if u not in y:
                    y.append(j)
                else:
                    if(u!=j and d!=j):
                        y.append(j)
        print(i)
        y.append(i)
        t.append(y)

print (e)
print(t)
print(o)
