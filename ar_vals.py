import numpy as np
a=[]
g=int(input('enter no of elements'))
for i in range(g):
        ele=int(input('enter elements'))
        a.append(ele)
#a=np.array([3,0,1,-1])
print(a)
l=len(a)
mini=100
maxi=0
f=0
o=0
p=0
for i in range(l):
    if(a[i]<mini and a[i]>=0):
        mini=a[i]
        p=1
if(p==0):
        mini=0
#print(mini)
for i in range(l):
    if(a[i]>maxi):
        maxi=a[i]
while (1):
        o=0
        #mini=mini+1
        for i in range (l):
                if(a[i]==mini):
                        
                        mini=mini+1
                        o=1
                        print(mini)
        #print("***")
        #mini=mini+1
        if(o==0):
                f=mini
                print("***")
                break

        #print("*")


        #break
    
    
if(mini>maxi):
        f=mini

print(f)




