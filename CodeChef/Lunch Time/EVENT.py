t=int(input())
days=[ "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
for i in range(t):
    s,e,l,r=map(str,input().split(" "))
    l=int(l)
    r=int(r)
    in1=days.index(s)
    in2=days.index(e)
    value=in2-in1+1
    if value<=0:
       value=value+7
    while value<l:
        value=value+7
    if l<=value+7 and value+7<=r:
       print("many")
       continue
    if value>=l and value<=r:
       print(value)
    if value>r:
        print("impossible")
        continue
