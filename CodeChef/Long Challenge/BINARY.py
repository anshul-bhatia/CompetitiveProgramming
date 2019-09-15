from sys import stdin,stdout
t=int(stdin.readline())
for _ in range(t):
    n,z=map(int,stdin.readline().split())
    l=list(map(int,stdin.readline().split()))
    ll=l[:]
    for i in range(z):
        for j in range(0,n-1):
            if l[j]==0 and l[j+1]==1:
                ll[j],ll[j+1]=ll[j+1],ll[j]
        l=ll[:]
    print(*l)
