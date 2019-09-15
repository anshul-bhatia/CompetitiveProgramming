t=int(input())
for _ in range(t):
    a=int(input())
    s=1
    d=1
    suma=a
    v=1
    di=dict()
    while(True):
        if s>suma:
            break
        else:
            suma+=a
            v*=2
            s=s+v
            d+=1
            if suma-s in di:
                continue
            else:
                di[suma-s]=d
    mx=max(di.keys())
    val=di[mx]
    print(d-1,val)
