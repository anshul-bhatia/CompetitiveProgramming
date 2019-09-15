t=int(input())
for _ in range(t):
    n,q,k,l,r=map(int,input().split())
    ans=[]
    li=[]
    lcp=[]
    for i in range(n):
        c,p=map(int,input().split())
        lcp.append([c,p])
    li=lcp[:]
    for j in range(1,q+1):
        
        ll=[]
        for i in range(n):
            li=lcp[:]
            for oo in range(j):
                if li[i][0]>k+1:
                    li[i][0]-=1
                elif li[i][0]<k-1:
                    li[i][0]+=1
                elif li[i][0]<=k+1 and li[i][0]>=k-1:
                    li[i][0]=k
            print(li[i][0],l,r)
            if li[i][0]>=l and li[i][0]<=r:
                ll.append(li[i][1])
                print(ll)
            #print(ll)
        if len(ll)==0:
            ans.append(-1)
        else:
            ans.append(min(ll))
    print(ans)
