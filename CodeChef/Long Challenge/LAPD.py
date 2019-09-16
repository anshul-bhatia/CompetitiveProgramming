import time
t=int(input())
mod=1000000007
##st=time.time()
for _ in range(t):
    count=0
    A,B,C=map(int,input().split())
    A=A-1
    C=C-1
    l=[]
    for i in range(1,B+1):
        l.append(i**2)
##    print(l)
    for j in range(1,B+1):
        for i in range(1,A+1):
            if j*j<i:
                count=(count+(A+1-i)*(C))%mod
                break
            for k in range(1,C+1):
                if j*j<i*k:
                    count=(count+C+1-k)%mod
                    break
    print(count)
##print(time.time()-st)
