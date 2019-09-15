for _ in range(int(input())):
        a1,a2,a3,c1,c2,c3=map(int,input().split())
	l=[[a1,c1],[a2,c2],[a3,c3]]
	l.sort()
	flag=0
	if l[0][0]==l[1][0] and l[0][1]!=l[1][1]:
		flag=1
	if l[1][0]==l[2][0] and l[1][1]!=l[2][1]:
		flag=1
	if l[0][0]<l[1][0] and l[0][1]>=l[1][1]:
		flag=1
	if l[1][0]<l[2][0] and l[1][1]>=l[2][1]:
		flag=1
	if flag==1:
		print("NOT FAIR")
	else:
		print("FAIR")
