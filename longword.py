import string
def LongestWord(sen): 

    # code goes here
    o=sen.split(' ')
    l=len(o)
    for j in range(l):
      for i in o[j] :
        if i in string.punctuation:
          #print(i)
          o[j]= o[j].replace(i,'')
    #pos=[1,1,1,1,1,1]
    m=0
    max=0
    min=1000
    count=0
    for i in range (l):
      #print(o[i])
      d=len(o[i])
      if(d>max):
        max=d
        pos=i
        #print(pos)
    
    for i in range(l):
      if(len(o[i])==max):
        #print(o[i])
        if(i<min):
          min=i
        count=count+1
        f=o[i]
        m=m+1
    if(count==1):
      v=o[pos]
    elif(count>1):
      #print (count)
      #print(min)
      v=o[min]
    
    return v
    
# keep this function call here  
print(LongestWord(input()))