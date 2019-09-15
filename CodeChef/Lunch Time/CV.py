d={}
st='qwertyuiopasdfghjklzxcvbnm'
for i in st:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        d[i]=1
    else:
        d[i]=0
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    count=0
    for i in range(n-1):
        if d[s[i]]==0 and d[s[i+1]]==1:
            count+=1
    print(count)
