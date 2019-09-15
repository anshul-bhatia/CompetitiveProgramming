from sys import stdin,stdout
t=int(stdin.readline())
mod=1000000007
for _ in range(t):
    n,k=map(int,stdin.readline().split())
    a=k-n
    d=1-n
    terms=a//abs(d)+1
    answer=(k-1+((terms*((2*a)+(terms-1)*d))//2)%mod)%mod
    print(answer)
