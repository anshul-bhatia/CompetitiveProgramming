#import bisect
t=int(input())
for _ in range(t):
    n=int(input())
    l=[]
    lf=[]
    lr=[]
    for i in range(n):
        s=input()
        l.append(s)
    stls=0
    strs=0
    for i in range(n):
        sl=0
        sr=0
        for j in range(n//2):
            sl+=int(l[i][j])
            sr+=int(l[i][(n//2)+j])
        lf.append(sl)
        lr.append(sr)
        stls+=sl
        strs+=sr
        ans=abs(stls-strs)
    lfin=[ans]
    for i in range(n):
        sq=stls-lf[i]+lr[i]
        sw=strs+lf[i]-lr[i]
        lfin.append(abs(sq-sw))
    print(min(lfin))
