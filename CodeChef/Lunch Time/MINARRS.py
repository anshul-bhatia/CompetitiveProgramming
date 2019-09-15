t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    ll=[]
    le=[]
    lo=[]
    coe=0
    coo=0
    l1=l[:]
    for i in range(n):
        if l[i]%2==0:
            coe+=1
            le.append(l[i])
        else:
            coo+=1
            lo.append(l[i])
    if coe>coo:
        val=min(le)
        val1=max(le)
    elif coo>coe:
        val=min(lo)
        val1=max(lo)
    else:
        if min(le)>min(lo):
            val=min(lo)
        else:
            val=min(le)
        if max(le)>max(lo):
            val1=max(le)
        else:
            val1=max(lo)
    for i in range(n):
        l[i]=l[i]^val
        l1[i]=l1[i]^val1
    if sum(l)<sum(l1):
        print(sum(l))
    else:
        print(sum(l1))
    for i in range(n):
        l[i]=l[i]^6
    print(sum(l))
