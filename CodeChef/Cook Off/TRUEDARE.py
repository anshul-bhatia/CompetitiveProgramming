t=int(input())
for i in range(t):
    tr=int(input())
    Tr=input()
    Tr=list(map(int,Tr.split()))

    dr=int(input())
    Dr=input()
    Dr=list(map(int,Dr.split()))

    ts=int(input())
    Ts=input()
    Ts=list(map(int,Ts.split()))

    ds=int(input())
    Ds=input()
    Ds=list(map(int,Ds.split()))

    flag=0
    for j in range(0,ts):
        if Ts[j] not in Tr:
            flag=1
            break
    
    for j in range(0,ds):
        if Ds[j] not in Dr:
            flag=1
            break
    

    if flag==1:
        print("no")
    else:
        print("yes")
        
    
