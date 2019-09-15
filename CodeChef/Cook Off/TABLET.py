t=int(input())
for _ in range(t):
    n,b=map(int,input().split())
    wl=[]
    hl=[]
    pl=[]
    for i in range(n):
        w,h,p=map(int,input().split())
        if p<=b:
            wl.append(w*h)
        else:
            continue
    if len(wl)==0:
        print("no tablet")
    else:
        print(max(wl))
