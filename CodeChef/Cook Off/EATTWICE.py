t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    d=dict()
    for i in range(n):
        di,v=map(int,input().split())
        if di in d:
            if v>d[di]:
                d[di]=v
        else:
            d[di]=v
    l=list(d.values())
    l.sort(reverse=True)
    print(l[0]+l[1])
