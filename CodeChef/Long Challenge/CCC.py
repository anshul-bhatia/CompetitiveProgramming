t=int(input())
for _ in range(t):
    n,z=map(int,input().split())
    l=list(map(int,input().split()))
##    s=l[:]
##    s=set(s)
##    s=list(s)
    l.sort(reverse=True)
    li=[0]*n
    li[0]=l[0]
    for i in range(1,len(l)):
        if l[i]==l[i-1]:
            li[i]=li[i-1]
        else:
            li[i]=(i+1)*l[i]
    print(min(li))
##    l.sort()
##    mx=l[len(l)-1]
##    if l.count(mx)>1:
##        print(mx)
##    else:
##        mx1=l[n-2]
##        if mx-mx1>=(n-1)*l[0]:
##            print(2*mx1)
##        else:
##            print(mx)
