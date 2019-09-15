import collections
t=int(input())
for _ in range(t):
    ll=[]
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    c=collections.Counter(a)
    count=0
    for i in c:
        if c[i]>=k:
            count=1
    if count==0:
        print(-1)
    else:
        for i in c:
            if c[i]>=k:
                l=[]
                for j in range(n):
                    if a[j]==i:
                            l.append(j)
                v=len(l)
                lll=l[:]
                lll.sort()
                if v%2==0:
                    val=v//2
                else:
                    val=v//2+1
                suml=0
                value=l[val-1]
                for i in range(v):
                    suml+=abs(l[i]-value-1)
                ll.append(suml)
        print(ll)
        if k%2!=0:
            mn=min(ll)
            ll.remove(mn)
            print(min(ll))
        else:
            print(min(ll))
