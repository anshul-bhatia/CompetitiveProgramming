t=int(input())
for _ in range(t):
    x,y,k=map(int,input().split())
    ans=(x+y)//k
    if ans%2==0:
        print("Chef")
    else:
        print("Paja")
