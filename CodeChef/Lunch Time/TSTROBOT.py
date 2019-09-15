t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    s=input()
    val=x
    ss=set()
    ss.add(val)
    for i in range(n):
        if s[i]=='L':
            val=val-1
            ss.add(val)
        if s[i]=='R':
            val=val+1
            ss.add(val)
    print(len(ss))
