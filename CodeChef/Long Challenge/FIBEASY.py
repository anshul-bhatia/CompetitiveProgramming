import math
l=[0]*61
l[0]=0
l[1]=1
l[2]=1
ll=[0]*61
ll[0]=0
ll[1]=1
ll[2]=1
for i in range(3,61):
    l[i]=(l[i-1]+l[i-2])
for i in range(3,61):
    ll[i]=(ll[i-1]+ll[i-2])%10
#print(ll)
def pow(n): 
    if (n < 1):
        return 0
    ans=1
    for i in range(60): 
        temp = 1 << i
        if (temp > n):
             break
        ans = temp
    return ans
def fiboLast(n):
    return ll[n%60]
t=int(input())
for _ in range(t):
    n=int(input())
    ans=pow(n)
    #print(ans)
    print(fiboLast(ans-1))
