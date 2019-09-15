t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    a=[0]*(n+1)
    s=0
    for i in range(n+1):
        a[i]=i
    for i in range(q):
        l=list(map(int,input().split()))
        if len(l)==2:
            a[s+l[1]]=0
        else:
            print(max(a[l[1]+s:l[2]+s+1]))
            s=(s+max(a[l[1]+s:l[2]+1+s])%n)%n
