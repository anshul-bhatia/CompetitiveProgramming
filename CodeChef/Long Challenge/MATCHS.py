from sys import stdin,stdout
t=int(stdin.readline())
for _ in range(t):
    n,m=map(int,stdin.readline().split())
    if m>n:
        n,m=m,n
    count=0
    l=[]
    if n==m:
        stdout.write("Ari"+'\n')
        continue
    while(True):
        if m==0 or n==0:
            break
        #print(n//m)
        l.append(n//m)
        n=n%m
        n,m=m,n
        #print(m)
    ln=len(l)
    #print(l)
    val=-1
    for i in range(ln):
        if l[i]>1:
            val=i+1
            break
    #if ln==1:
    #    stdout.write("Ari"+'\n')
    #    continue
    if val==-1:
        if (ln)%2==0:
            stdout.write("Rich"+'\n')
        else:
            stdout.write("Ari"+'\n')
    else:
        if val%2==0:
            stdout.write("Rich"+'\n')
        else:
            stdout.write("Ari"+'\n')
