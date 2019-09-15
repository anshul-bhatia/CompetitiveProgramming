from sys import stdin,stdout
mod=1000000007
t=int(stdin.readline())
def power(x, y) : 
    ans = 1  
    x = x % mod  
    while (y > 0) : 
 
        if ((y & 1) == 1) : 
            ans = (ans * x) % mod  
        y = y >> 1
        x = (x * x) % mod
    return ans%mod 
for _ in range(t):
    k=int(stdin.readline())
    stdout.write(str((10*power(2,k-1))%mod)+'\n')
