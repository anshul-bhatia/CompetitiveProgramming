t=int(input())
for _ in range(t):
    n=int(input())
    l= list(map(int,input().split()))
    ll=[]
    li=[0]*n
    for i in range(n-3):
        if 2*(l[i+1]-l[i]) == l[i+3]-l[i+1]:
            d=l[i+1]-l[i]
            break
        else:
            if 2*(l[i+1]-l[i]) == l[i+2]-l[i]:
                d=l[i+2]-l[i+1]
                break
    answer=[-999,-999]
    if l[1]-l[0]!=d:
        if l[2]-l[i]==d:
            answer=[l[0],l[1]-d]
        else:
            answer=[l[1],l[0]+d]
    for i in range(1,n-2):
        if l[i+1]-l[i]!=d:
            ans=l[i]+d
            if l[i+2]-ans==d:
                answer=tuple((l[i+1],ans))
                break
    if l[n-1]-l[n-2]!=d:
        if l[n-1]-l[n-3]!=2*d:
            answer=[l[n-1],l[n-2]+d]
    for i in range(n):
        if l[i]==answer[0]:
            print(answer[1],end=" ")
        else:
            print(l[i],end=" ")
    print()
