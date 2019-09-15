from collections import defaultdict
mod=1000000007
def fx(n):
    s=0
    if len(n)==1:
        return int(n[0])
    for i in range(len(n)-1):
        if n[i+1]==n[i]:
            continue
        else:
            s=(s+(int(n[i])*(10**i)))%mod
    s=(s+(int(n[len(n)-1])*(10**(len(n)-1))))%mod       
    return s
t=int(input())
for _ in range(t):
    nl,l=map(int,input().split())
    nr,r=map(int,input().split())
    s=0
##    ls=[i for i in str(l)][::-1]
##    s+=fx(ls)
##    print(ls)
    for i in range(l,r+1):
        s=(s+fx([j for j in str(i)][::-1]))%mod
    print(s)
    
        
