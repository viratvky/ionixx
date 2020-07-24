d={}
while(1):
    try:
        print("Enter source to dest like A-B")
        a,b=input().split('-')
        print("Enter the input like this format 30 50")
        c,k=map(int,input().split())
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
print(d)
        
        
