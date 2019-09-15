t=int(input())
for _ in range(t):
    n=int(input())
    k=int(input())
    if n<k:
        extra=k%n
        ans=n-extra
    else:
        extra=k
        ans=n-k
    if ans<extra:
        ans,extra=extra,ans
    if ans>=extra+1:
        print(2*extra)
    else:
        print(ans+ans-1)
