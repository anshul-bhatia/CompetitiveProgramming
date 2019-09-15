t=int(input())
for _ in range(t):
    s=input()
    ln=len(s)
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    l=list(d.values())
    count=0
    counte=0
    for i in l:
        if i%2!=0:
            count+=1
        else:
            counte+=1
    if ln%2==0:
        if count>2 or count==0:
            print("!DPS")
        else:
            print("DPS")
    else:
        if count<=3:
            print("DPS")
        else:
            print("!DPS")
