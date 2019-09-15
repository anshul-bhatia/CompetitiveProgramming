t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    l=[]
    val=0
    for i in range(n):
        val=i
        suml=0
        while(val<n):
            if val<n:
                suml+=a[val]
            if val+k>=n:
                break
            val+=k
        l.append(suml)
    print(max(l))
