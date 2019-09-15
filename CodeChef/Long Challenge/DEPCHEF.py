t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d=list(map(int,input().split()))
    l=[]
    val=d[0]-a[1]-a[n-1]
    if val>0:
        l.append(d[0])
    val=d[n-1]-a[0]-a[n-2]
    if val>0:
        l.append(d[n-1])

    for j in range(1,n-1):
        val=d[j]-a[j-1]-a[j+1]
        if val>0:
            l.append(d[j])
    if len(l)==0:
        print("-1")
    else:
        print(max(l))
