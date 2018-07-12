a,b=input().split()
a=int(a)
b=int(b)
for x in range(a,b):
	temp=x
	num=0
	while x!=0:
		y=x%10
		x=x//10
		num += y**3
	if num==temp:
		print(temp,end=" ")
