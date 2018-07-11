x,y=input().split()
x=int(x)
y=int(y)
for z in range(x+1,y):
	count=0
	for i in range(1,z+1):
		if z%i==0:
			count=count+1
	if count==2:
		print (z,end=" ")
