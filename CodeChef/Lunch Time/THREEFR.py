t=int(input())
for i in range(t):
    a=input()
    x,y,z=map(int,a.split())
    if x+z==y or x+y==z or y+z==x:
        print("yes")
    else:
        print("no")
