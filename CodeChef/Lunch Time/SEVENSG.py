t=int(input())
for _ in range(t):
    d={}
    d[0]=6
    d[1]=2
    d[2]=5
    d[3]=5
    d[4]=4
    d[5]=5
    d[6]=6
    d[7]=3
    d[8]=7
    d[9]=6
    n=int(input())
    for i in range(n):
        xi,yi=map(int,input().split())
        if yi>d[xi]:
            print("invalid")
            break
        v=d[xi]-yi
        mn=v
        mx=7-yi
        print(mn,mx)
