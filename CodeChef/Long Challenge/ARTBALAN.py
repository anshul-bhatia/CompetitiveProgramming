def prime(n):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	return False
    return True
t=int(input())
for i in range(t):
    s=input()
    l=[]
    for j in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        c=s.count(j)
        l.append(c)
    if prime(len(s)):
        print(len(s)-max(l))
    else:
        
