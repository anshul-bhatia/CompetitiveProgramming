from collections import *
def fact(n):
    if n==0:
        return 1
    ans=1
    for i in range(2,n+1):
        ans=ans*i
    return ans
def ncr(n,r):
    return fact(n)//(fact(n-r)*fact(r))
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    d=defaultdict(int)
    dd=defaultdict(int)
    minsum=sum(a[:k])
    aa=a[:k]
    #print(minsum)
    for i in a:
        d[i]+=1
    #print(d)
    for i in range(k):
        dd[aa[i]]+=1
    total=1
    for i in dd:
        total=total*ncr(d[i],dd[i])
    print(total)
