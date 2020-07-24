d={}
while(1):
    try:
        print("Enter source to dest like A-B")
        a,b=input().split('-')
        print("Enter the input like this format 30 50")
        c,k=map(int,input().split())
        a1=''
        b1=''
        c1=''
        d1=''
        if a=='A':
            a1=a1+b
        if a=='B':
            b1=b1+b
        if a=='C':
            c1=c1+b
        if a=='D':
            d1=d1+b        
        try:
            if d[a]>c*k:
                d[a]=c*k
        except:
            d[a]=c*k
        try:
            if d[b]>c*k:
                d[b]=c*k
        except:
            d[b]=c*k
    except:
        break
l=[]
for i in d:
    l.append(d[i])
print(min(l))
        
        
