from sys import stdin,stdout
l=[0]*1000001
l[1]=1
l[2]=5
for i in range(3,1000001):
    l[i]=(l[i-1]+i+l[i-1]*i)%1000000007
    t=int(stdin.readline())
    for _ in range(t):
        n=int(stdin.readline())
    stdout.write(str(l[n])+'\n')
