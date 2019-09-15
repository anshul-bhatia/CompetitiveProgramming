t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    if a[0]>0:
        print(len(a),len(a))
    else:
        count1=0
        count2=0
        for i in range(n):
            if a[i]<0:
                count1+=1
            else:
                count2+=1
        if count1>count2:
            print(count1,count2)
        else:
            print(count2,count1)
