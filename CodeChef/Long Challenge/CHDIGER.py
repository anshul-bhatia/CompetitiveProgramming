t=int(input())
for _ in range(t):
    n,d=map(int,input().split())
    s=str(n)
    l=[]
    ll=[]
    st=''
    dif=0
    for i in s:
        l.append(int(i))
    ln=len(l)
    mn=min(l)
    while mn<=d:
        if len(l)>0:
            mn=min(l)
            ind=l.index(mn)
            if mn>d:
                break
            if mn<d:
                ll.append(l[ind])
            l=l[ind+1:ln]
            ln=len(l)
        else:
            break
    dif=len(s)-len(ll)
    st=''.join(str(i) for i in ll)
    st=st+str(d)*dif
    print(st)
