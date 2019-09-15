t=int(input())
for o in range(t):
    n=int(input())
    set1=set()
    set2=set()
    l=[]
    di=dict()
    li=[]
    for i in range(n):
        s=input()
        l.append(s)
    for i in range(len(l[0])):
        di[l[0][i]]=1
    for i in range(1,n):
        for j in range(len(l[i])):
            if di.get(l[i][j])==1:
                
                
    count=0
    for i in di:
        if di[i]==n:
            count+=1
    print(count)
