def subs(string):
    length = len(string)
    l = []
    for j in range(length):
        l.append(string[0:j + 1])
        if string[j]==string[0]:
            for k in range(j,length):
                l.append(string[j:k + 1])
    print(l)
    return l
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    l=subs(s)
    d=dict()
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    mx=max(d.values())
    ll=[]
    di=dict()
    for k in d:
        if d[k]==mx:
            di[k]=len(k)
            mxm=k
    for i in di:
        if len(i)>len(mxm):
            mxm=i
    print(mxm)
