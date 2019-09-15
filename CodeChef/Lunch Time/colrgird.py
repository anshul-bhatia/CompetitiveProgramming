t=int(input())
for i in range(t):
    a=input()
    l=[]
    n,m=map(int,a.split())
    for j in range(n):
        x=input()
        l.append(x)
        flag=1
    if '#' not in l[0]:
        print("YES")
        continue
    else:
        k=l[0]
        value=k.index('#')
        count=0
        for o in k:
            if o=='#':
                count+=1
        if count==1 and value>1 and value<len(k)-1-2 or value==len(k)-1:
            print("YES")
            continue
        else:
            if count>1:
                for z in range(len(k)-1):
                    if k[z]=='#':
                        if z<2:
                            flag=0
                            break
                        else:
                            if z-value<2:
                                flag=0
                                break
                            else:
                                value=z
                                continue
        if value<len(k)-1-2 or value==len(k)-1:
            if flag==1:
                print("YES")
            else:
                print("NO")
