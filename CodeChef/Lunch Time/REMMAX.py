t=int(input())
for _ in range(t):
    n=input()
    l=len(n)
    if l==1:
        print(n)
        continue
    if n.count('9')==l:
        print(n)
    else:
        val=int(n[0])
        if val==1:
            if n.count('0')==l-1:
                #s=str(int(n[0])-1)
                s=('9'*(l-1))
                print(s)
                continue
            else:
                count=0
                for i in range(1,l):
                    if n[i]=='0':
                        count+=1
                        continue
                    else:
                        break
                if count==l-2 and n[count+1]=='1':
                    s=('9'*(l-1))
                    print(s)
                    continue
                s=n[0:count+1]
                val=str(int(n[count+1])-1)
                s+=val
                ln=len(s)
                s+='9'*(l-ln)
                print(s)

        else:
            s=str(int(n[0])-1)
            s=s+('9'*(l-1))
            print(s)
