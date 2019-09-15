t=int(input())
for _ in range(t):
    d={}
    d['c']=0
    d['o']=0
    d['d']=0
    d['e']=0
    d['c']=0
    d['h']=0
    d['e']=0
    d['f']=0
    n=int(input())
    s=''
    for j in range(n):
        s+=input()
    for i in s:
        if i in d:
            d[i]+=1
    d['c']=d['c']//2
    d['e']=d['e']//2
    print(min(d.values()))
