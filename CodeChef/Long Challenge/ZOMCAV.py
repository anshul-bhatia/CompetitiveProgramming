t=int(input())
for _ in range(t):
    n=int(input())
    c=list(map(int,input().split()))
    h=list(map(int,input().split()))
    l=[0]*n
    ll=[0]*(n+2)
    for i in range(n):
        l[i]=[max(i-c[i],0),min(n-1,i+c[i])]
        if i+c[i]>=0:
            ll[l[i][0]]+=1
            ll[l[i][1]+1]-=1
    for i in range(1,n):
        ll[i]=ll[i-1]+ll[i]
    ll=ll[:n]
##    print(ll)
##    print(l)
    ll.sort()
    h.sort()
    if ll == h:
        print("YES")
    else:
        print("NO")
