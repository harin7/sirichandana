x=int(input())
temp=x
num=0
while x!=0:
	y=x%10
	x=x//10
	num += y**3
if num==temp:
	print("num is amstrong")
else:
	print("num is not amstrong")
