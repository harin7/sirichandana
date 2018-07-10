x=int(input())
y=x
count=0
while y!=0:
	if x%y==0:
		count=count+1
	y=y-1
if count==2:
	print("prime")
else:
	print("not prime")
