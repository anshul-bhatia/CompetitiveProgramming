t=int(input())
superset=set(('a','e','i','o','u'))
l=[('a',), ('a', 'e'), ('a', 'e', 'i'), ('a', 'e', 'o'), ('a', 'e', 'u'), ('a', 'i', 'o'), ('a', 'i', 'u'), ('a', 'o', 'u'), ('a','i'), ('a','o'), ('a','u'), ('e','o'), ('e','u'), ('i','u'), ('a', 'e', 'i', 'o'), ('a', 'e', 'i', 'u'),('a', 'e', 'o', 'u'), ('a', 'i', 'o', 'u'), ('e','i','o','u'), ('e',), ('e', 'i'), ('e', 'i', 'o'), ('e', 'i', 'u'), ('e', 'o', 'u'), ('e', 'i', 'o', 'u'), ('i',), ('i', 'o'), ('i', 'o', 'u'), ('o',), ('o', 'u'), ('u',)]
for i in l:
    d[i]=0
for _ in range(t):
    n=int(input())
    count=0
    counter=0
    ss=[]
    di=dict()
    for i in range(n):
        s=input()
        ss.append(s)
    for i in ss:
        li=set(i)
        li=list(li)
        li.sort()
        k=tuple(li)
        if k in di:
            di[k]+=1
        else:
            di[k]=1
    print(di)
    sumit=0
    for i in d:
        for j in di:
            flag=0
            val=list(superset-set(i))
            val.sort()
            val=tuple(val)
            
            for c in i:
                if c not in j:
                    flag=-1
                    break
                if flag==0:
                    d[i]+=di[j]
            sumit+=d[i]*
                    
      #      print(sumit)
    #print(sumit//2+counter*(n-counter)+((counter)*(counter-1))//2)
