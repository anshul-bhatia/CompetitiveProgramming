t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    ml=list(map(int,input().split()))
    suml=0
    l=[]
    ll=[0]*n
    suml=0
    di=dict()
    for i in range(n):
        d,f,b=map(int,input().split())
        l.append((d,f,b))
    for i in range(n):
        if ml[l[i][0]-1]>0:
            ll[i]=l[i][0]
            ml[l[i][0]-1]-=1
            suml+=l[i][1]
        else:
            suml+=l[i][2]
    for i in range(m):
        if ml[i]>0:
            di[i]=ml[i]
    for i in range(n):
        if ll[i]==0:
            for j in d:
                if d[j]>0:
                    ll[i]=j
                    d[j]-=1
    print(suml)
    print(*ll)
