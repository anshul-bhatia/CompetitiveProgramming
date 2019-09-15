t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    r=input()
    zs=s.count('0')
    zr=r.count('0')
    os=s.count('1')
    ore=r.count('1')
    if zs==zr and os==ore:
        print("YES")
    else:
        print("NO")
