n=int(input())
a=list(map(int,input().split()))
s=set(a)
l=list(s)
l.sort()
val=len(l)
ans=l[val-2]%l[val-1]
print(ans)
