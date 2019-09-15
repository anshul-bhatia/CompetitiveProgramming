t=int(input())
for _ in range(t):
    r,c = map(int,input().split())
    ll=[]
    for i in range(r):
        l=list(map(int,input().split()))
        ll.append(l)
    flag=0
    for i in range(r):
        for j in range(c):
            if i==0 or i==r-1:
                if j==0 or j==c-1:
                    if ll[i][j]>=2:
                        flag=-1
                else:
                    if ll[i][j]>=3:
                        flag=-1
            else:
                if j==0 or j==c-1:
                    if ll[i][j]>=3:
                        flag=-1
                else:
                    if ll[i][j]>=4:
                        flag=-1
    if flag==-1:
        print("Unstable")
    else:
        print("Stable")
