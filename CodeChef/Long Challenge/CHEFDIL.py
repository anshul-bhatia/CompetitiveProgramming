t=int(input())
for _ in range(t):
    s=input()
    if s.count('1')%2!=0:
        print("WIN")
    else:
        print("LOSE")
