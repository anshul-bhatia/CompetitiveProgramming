t=int(input())
for _ in range(t):
    n,m,k,l,r=map(int,input().split())
    ll=[]
    for i in range(n):
        c,p=map(int,input().split())
        for i in range(m):
            if c>k+1:
                c-=1
            elif c<k-1:
                c+=1
            elif c<=k+1 and c>=k-1:
                c=k
        if c>=l and c<=r:
            ll.append(p)
    if len(ll)==0:
        print(-1)
    else:
        print(min(ll))
