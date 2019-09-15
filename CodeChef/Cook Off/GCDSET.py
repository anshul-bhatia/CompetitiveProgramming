import math
t=int(input())
for _ in range(t):
    l,r,g=map(int,input().split())
    if(l//g==l/g):
        x=l//g-1
    else:
        x=l//g
    y=r//g
    #x=l//g
    #y=r//g
    #res=y-x
    #if(l%g==0):
        #y+=1
    if (y-x)==1:
        if g<l or g>r:
            print(0)
        else:
            print(1)
    else:
        print(y-x)
