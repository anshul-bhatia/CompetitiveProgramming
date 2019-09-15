t=int(input())
for _ in range(t):
    n=int(input())
    l= list(map(int,input().split()))
    dd={}
    for i in range(n-1):
        if l[i+1]-l[i] in dd:
            dd[l[i+1]-l[i]]+=1
        else:
            dd[l[i+1]-l[i]]=1
    ll=list(dd.keys())
    if len(ll)==1:
        print(*l)
        continue
    else:
        if len(ll)==2:
            d=l[2]-l[1]
            if l[1]-l[0]!=d:
                l[0]=l[1]-d
            else:
                l[n-1]=l[n-2]+d
            print(*l)
        else:
            d=(ll[0]+ll[1]+ll[2])//3
            for i in range(n-1):
                if l[i+1]-l[i]!=d:
                    l[i+1]=l[i]+d
                    break
            print(*l)
