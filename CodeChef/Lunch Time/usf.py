t=int(input())
for i in range(t):
    m=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    n=int(input())
    l=list(map(int,input().split()))
    usf=[]
    mso=[]
    for j in l:
        count=0
        if j in m:
            for k in range(0,len(l)):
                if l[k]%j==0:
                    mso.append(l[k])
                    count+=1
            usf.append(count)
    print(usf)
    print(max(usf))
