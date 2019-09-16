t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    maxm=(n*(n+1))//2
    if m>maxm or m<n-1:
        print(-1)
    elif n==1 and m==1:
        print(1)
    elif n==2 and m==1:
        print(1)
    elif n==1 and m==0:
        print(0)
    else:
        quo=m//n
        remainder=m%n
        val=n//2
##        print(quo,remainder)
##        print(val)
        if m<=n+1:
            print(2)
        elif m>n+1 and m<=2*n:
            print(3)
        elif m>quo*n and m<=quo*n+val:
            print(2*quo)
##            print(quo*n)
        elif m>quo*n+val and m<(quo+1)*n:
##            print((quo+1)*n)
            print(2*(quo)+1)
        else:
            print(2*quo-1)
