t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    d={}
    for i in range(k):
        r,c=map(int,input().split())
        tup=tuple((r,c))
        d[tup]=1
    fence=0
    for i in d:
        if (i[0]-1,i[1]) not in d:
            fence+=1
        if (i[0],i[1]-1) not in d:
            fence+=1
        if (i[0],i[1]+1) not in d:
            fence+=1
        if (i[0]+1,i[1]) not in d:
            fence+=1
    print(fence)
