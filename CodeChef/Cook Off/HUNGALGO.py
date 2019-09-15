t=int(input())
for _ in range(t):
    n=int(input())
    countr=0
    countc=0
    ll=[]
    for i in range(n):
        l=list(map(int,input().split()))
        ll.append(l)
    l1=ll[:]
    for i in range(n):
        if 0 in ll[i]:
            countr+=1
    for i in range(n):
        for j in range(n):
            l1[i][j]=ll[j][i]
    print(l1)
    for i in range(n):
        if 0 in l1[i]:
            countc+=1
    if countr==n and countc==n:
        print("YES")
    else:
        print("NO")
