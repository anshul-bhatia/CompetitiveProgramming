t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    u=input()
    c=0
    i=0
    while(i<n):
        if u[i]=='N':
            i+=1
            continue
        elif u[i]==s[i]:
            c+=1
            i+=1
        else:
            i+=2
    print(c)


