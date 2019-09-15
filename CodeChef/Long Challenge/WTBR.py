t=int(input())
for _ in range(t):
    n=int(input())
    ll=[0]*(n-1)
    lx=[]
    ly=[]
    lxx=[0]*n
    lyy=[0]*n
    for i in range(n):
        l=list(map(int,input().split()))
        lx.append(l[0])
        ly.append(l[1])
    for i in range(n):
        lxx[i]=ly[i]+lx[i]
        lyy[i]=ly[i]-lx[i]
    lxx.sort()
    lyy.sort()
    lly=[0]*(n-1)
    for i in range(n-1):
        ll[i]=abs(lxx[i+1]-lxx[i])/2
        lly[i]=abs(lyy[i+1]-lyy[i])/2
    print(min(min(ll),min(lly)))
