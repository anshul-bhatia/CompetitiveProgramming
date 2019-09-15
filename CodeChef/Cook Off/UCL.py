t=int(input())
for _ in range(t):
    ht=[]
    hg=[]
    at=[]
    ag=[]
    l=[]
    ll=[]
    d={}
    dd={} 
    for i in range(12):
        htn,htg,v,atg,atn=input().split()
        ht.append(htn)
        hg.append(int(htg))
        at.append(atn)
        ag.append(int(atg))
    s=set(ht)
    for i in s:
        d[i]=0
        dd[i]=0
    for i in range(12):
        if hg[i]>ag[i]:
            d[ht[i]]+=3
            dd[ht[i]]+=hg[i]-ag[i]
            dd[at[i]]+=ag[i]-hg[i]
        elif hg[i]<ag[i]:
            d[at[i]]+=3
            dd[at[i]]+=ag[i]-hg[i]
            dd[ht[i]]+=hg[i]-ag[i]
        else:
            d[ht[i]]+=1
            d[at[i]]+=1
    for i in d:
        l.append((d[i],dd[i],i))
    l.sort()
    print(l[3][2],l[2][2])
