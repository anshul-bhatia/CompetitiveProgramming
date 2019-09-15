import math
t=int(input())
for _ in range(t):
    D=int(input())
    s=input()
    count=0
    required=math.ceil(D*0.75)
    for i in s:
        if i=='P':
            count+=1
    if count>=required:
        print(0)
        continue
    coa=0
    for i in range(2,D-2):
        if s[i]=='A':
            if (s[i-1]=='P' or s[i-2]=='P') and (s[i+1]=='P' or s[i+2]=='P'):
                coa+=1
    if coa+count>=required:
        print(required-count)
    else:
        print(-1)
