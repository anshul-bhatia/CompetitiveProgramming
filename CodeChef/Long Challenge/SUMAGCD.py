import math
from sys import stdin,stdout
t=int(stdin.readline())
for _ in range(t):
    n=int(stdin.readline())
    l=list(map(int,stdin.readline().split()))
    s=set(l)
    ln=len(s)
    s=list(s)
    s.sort()
    l.sort()
    mx=s[-1]
    if n==2:
        gcd=l[0]
    else:
        if ln>2:
            s=s[:ln-1]
            gcd=math.gcd(s[0],s[1])
        else:
            gcd=s[0]

    for i in range(2,ln-1):
        if gcd==1:
            break
        else:
            gcd=math.gcd(gcd,s[i])
    stdout.write(str(gcd+mx)+'\n')
