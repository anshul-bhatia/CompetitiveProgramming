t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    while(len(l)!=1):
        m=l[0]+l[1]
        ind=0
        indd=1
        for i in range(1,len(l)-1):
            val=l[i]+l[i+1]
            #print(val)
            if val<m:
                m=val
                ind=i
                indd=i+1
        
        if l[0]+l[len(l)-1]<m:
            m=l[0]+l[len(l)-1]
            ind=0
            indd=len(l)-1
##        print("m",m)
        s+=m
        l.insert(ind,m)
        l.remove(l[ind+1])
        l.remove(l[indd])
##        print(l)
    print(s)
