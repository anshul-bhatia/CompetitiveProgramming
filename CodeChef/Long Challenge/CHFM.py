t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=sum(l)
    mean=s/n
    ll=[]
    for i in range(n):
        if (s-l[i])/(n-1)==mean:
            ll.append((l[i],i+1))
    if len(ll)==0:
        print("Impossible")
    else:
        print(min(ll)[1])
