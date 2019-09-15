t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    sumll=0
    for i in range(n):
        sumll+=(a[i]+b[i])//2 
    #a.sort(reverse=False,key=fn)
    #b.sort(reverse=False,key=fn1)
    suml=0
    su=0
    coa=0
    cob=0
    cea=0
    ceb=0
    for i in range(n):
        if a[i]%2!=0:
            coa+=1
        else:
            cea+=1
        if b[i]%2==0:
            ceb+=1
        else:
            cob+=1
    ans=min(coa,cob)
    a1=max(coa,cob)-ans
    print((sum(a)+sum(b))//2-int(a1*0.5))
