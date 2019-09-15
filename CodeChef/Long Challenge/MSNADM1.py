t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=[0]*n
    for i in range(n):
        l[i]=(a[i]*20)-b[i]*10
    if max(l)<0:
        print(0)
    else:
        print(max(l))
