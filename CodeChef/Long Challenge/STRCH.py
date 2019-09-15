t=int(input())
for _ in range(t):
    n=int(input())
    l=[]
    s,x=input().split()
    for i in range(n):
        if s[i]==x:
            l.append(i)
    ln=len(l)
    if ln==0:
        print(0)
        continue
    suml=(l[0]*(l[0]+1))//2
    suml+=(((n-1-l[ln-1]))*(n-l[ln-1]))//2
    for i in range(ln-1):
        val=l[i+1]-l[i]-1
        suml+=(val*(val+1))//2
    print((n*(n+1))//2-suml)
