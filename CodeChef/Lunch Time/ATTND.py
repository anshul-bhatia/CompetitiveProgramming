t=int(input())
for _ in range(t):
    n=int(input())
    l=[]
    lf=[]
    for i in range(n):
        f,ll=map(str,input().split())
        tt=tuple((f,ll))
        lf.append(f)
        l.append(tt)
    for i in range(n):
        
        if (lf.count(l[i][0]))>1:
            print("{} {}".format(l[i][0],l[i][1]))
        else:
            print(l[i][0])
