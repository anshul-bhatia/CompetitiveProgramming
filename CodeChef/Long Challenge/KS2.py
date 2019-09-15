t=int(input())
for _ in range(t):
    n=input()
    ln=len(n)
    suml=0
    for i in range(ln):
        suml+=int(n[i])
    answer=10-suml%10
    if answer==10:
        n+='0'
    else:
        n+=str(answer)
    print(n)
