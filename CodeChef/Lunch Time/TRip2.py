for _ in range(int(input())):
	n,k=map(int,input().split())
	l=list(map(int,input().split()))
	flag=0
	for i in range(n):
		# print(i)
		if l[i]==-1:
			if i==0:
				j=1
				while(j<k):
					if j!=l[i+1]:
						l[i]=j
						break
					else:
						j+=1
				else:
					print("NO")
					flag=1
					break
			elif i!=n-1:
				j=1
				while(j<k):
					# print(j)
					if j!=l[i+1] and j!=l[i-1]:
						l[i]=j
						break
					else:
						j+=1
				else:
					print("NO")
					flag=1
					break
			else:
				j=1
				while(j<k):
					if j!=l[i-1]:
						l[i]=j
						break
					else:
						j+=1
				else:
					print("NO")
					flag=1
					break
	if flag==0:
		print("YES")
		print(*l)
