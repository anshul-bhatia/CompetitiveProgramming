t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.insert(0,0)
    count=0
    a.sort()
    for i in range(1,n+1):
        if a[i]==0:
            count+=1
        else:
            if a[i]<=count:
                count+=1
    print(count)
