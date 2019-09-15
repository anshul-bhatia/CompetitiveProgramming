l=dict()
n,m=map(int,input().split())
ln=list(map(int,input().split()))
lm=list(map(int,input().split()))
total=n+m-1
l1=len(ln)
l2=len(lm)
value1=lm.index(min(lm))
for k in range(l1):
    print("{0} {1}".format(k,value1))
value2=ln.index(max(ln))
temp=min(lm)
for k in range(l2):
    if lm[k]==temp:
        continue
    else:
        print("{0} {1}".format(value2,k))
