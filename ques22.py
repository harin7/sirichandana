x=int(input("enter the num"))
y=[int(i) for i in input().split()]
max=y[0]
for j in range(0,x):
	if y[j]>max:
		max=y[j]
print(max)
