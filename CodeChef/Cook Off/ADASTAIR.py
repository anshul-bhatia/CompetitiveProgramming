t=int(input())
for i in range(t):
    l=input()
    n,k=map(int,l.split())
    H=input()
    count=0
    h=list(map(int,H.split()))
    temp=h[0]
    while temp>k:
        temp=temp-k
        count+=1
        #value=h[0]-k
        #count+=value//k
    for x in range(len(h)-1):
        while h[x+1]-h[x]>k:
            h[x]+=k
            count+=1

    print(count)
