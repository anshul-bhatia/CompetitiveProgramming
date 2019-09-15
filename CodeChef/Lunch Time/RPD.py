def digitsum(n):
    s=0
    while(n!=0):
        s+=n%10
        n=n//10
    return s
t=int(input())
for _ in range(t):
    n=int(input())
    ll=[]
    l=list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            ans=l[i]*l[j]
            ll.append(digitsum(ans))
    print(max(ll))
