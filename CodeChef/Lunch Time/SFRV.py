t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    ll=l[:]
    lll=[]
    j=0
    while(j<n-1):
        i=j
        l=ll[:]
        while(i<n):
            if i+1>=n:
                break
            elif l[i]>l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
                i+=2
            else:
                i+=1
        s=0
        print(l)
        for i in range(n):
            s+=l[i]*(i+1)
        lll.append(s)
        j+=1
    print(lll)
    print(max(lll))
