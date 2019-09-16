from collections import *
from math import factorial as f
def nCr(n,r):
    return f(n)//(f(n-r)*f(r))
mod=1000000007
n,k=map(int,input().split())
a=list(map(int,input().split()))
##a.sort()
##d=defaultdict(int)
##for i in a:
##    d[i]+=1
count=0
for i in range(k+1):
##    print(nCr(n,i),n,i)
    count=(count+nCr(n,i))%mod
##total=sum(d.values())
##print(total)
##print(d)
print(count)
