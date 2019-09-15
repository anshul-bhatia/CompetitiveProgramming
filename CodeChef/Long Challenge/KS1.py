from collections import defaultdict
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    l=[0]*n
    l[0]=a[0]
    for i in range(1,n):
        l[i]=l[i-1]^a[i]
    d=defaultdict(list)
    cc=0
    cz=0
    for i in range(n):
        d[l[i]].append(i)
        if l[i]==0:
            cz+=i
    for i in d:
        if len(d[i])>1:
            cz-=(len(d[i])*(len(d[i])-1))//2
        for j in range(len(d[i])-1,-1,-1):
            cz+= (j*d[i][j]-(len(d[i])-1-j)*d[i][j])
    print(cz)
