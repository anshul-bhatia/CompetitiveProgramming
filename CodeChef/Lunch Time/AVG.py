import math
t=int(input())
for _ in range(t):
    n,k,v=map(int,input().split())
    l=list(map(int,input().split()))
    s=sum(l)
    ni=(v*(n+k)-s)/k
    if int(ni)==ni and ni>0:
        print(int(ni))
    else:
        print(-1)
