def  bits(n): 
    c = 0
    while (n): 
        c+= n & 1
        n >>= 1
    return c 
t=int(input())
for _ in range(t):
    q=int(input())
    s=set()
    ev=0
    odd=0
    for i in range(q):
        x=int(input())
        if x in s:
            print(ev,odd)
            continue
        val=bits(x)
        #print(val)
        s.add(x)
        if val%2==0:
            ev+=1
        else:
            odd+=1
        ss=set()
        for j in s:
            if j==x:
                continue
            a=j^x
            if a not in s:
                va=bits(a)
                #print(va)
                #print(a,va)
                if va%2==0:
                    ev+=1
                else:
                    odd+=1
                ss.add(a)
        s=s.union(ss)
        #print(s)
        print(ev,odd)
