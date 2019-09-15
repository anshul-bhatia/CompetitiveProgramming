t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    la=[0]*n
    lb=[0]*n
    la[0]=a[0]
    lb[0]=b[0]
    lll=[]
    for i in range(1,n):
        la[i]=la[i-1]+a[i]
        lb[i]=lb[i-1]+b[i]
    lll.append(la[n-1])
    lll.append(lb[n-1])
    for i in range(n):
        lll.append(la[i]+lb[n-1]-lb[i])
    print(max(lll))
