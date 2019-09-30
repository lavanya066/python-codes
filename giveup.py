a=123
q=[]

h=10
r=a%100
for i in range(len(str(a))):
    w=[]
    d=int(a%100)
    w.append(d)
    x=int(a)
    #print (a)
    #print("val ofa")
    m=x
    
    
    while(m>0):
        
        e=int(m%10)
        
        w.append(e)
        print (w)
        m=int(m/10)
    w.reverse()
    
    #a=int(a/10)
    for o in w:
        print(o)
        if o not  in q:
             
            q.append(o)
    
    h*=10
    a=int(a/10)
#q.append(r)
e=[]
y=[]
t=[]
for i in q:
    if(len(str(i))==1):
        print(i)
        e.append(i)
        print("****")
    if(len(str(i))==2):
        u=int(i%10)
        d=int(i/10)
        y=[]
        for j in q:
            
            if u!= j and d != j and len(str(j))==1:
                print(j)

                y.append(j)
        print(i)
        y.append(i)
        t.append(y)
print(q)
print (e)
print(t)
