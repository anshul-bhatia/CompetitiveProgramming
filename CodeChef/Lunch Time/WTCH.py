t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    count=0
    l=[]
    for j in range(n):
        if(s[j]=='1'):
            l.append(j)
            count=count+1
    if count==0:
        if n%2==0:
            print(n//2)
        else:
            print(n//2+1)
    else:
        count=0
        for j in range(len(l)-1):
            m=l[j+1]-l[j]
            if m>2:
                if m%2!=0:
                       count+=m//2
                else:
                    count+=m//2-1
        if 0 not in l:
            m=l[0]
            print(m)
            if m==2 or m==3:
                count+=1
            if m>3:
                if m%2!=0:
                    count+=m//2
                else:
                    count+=m//2-1
        if n-1 not in l:
            m=n-1-l[-1]
            if m==2 or m==3:
                count+=1
            if m>3:
                print(m)
                if m%2!=0:
                    count+=m//2
                else:
                    count+=m//2
        print(count)
