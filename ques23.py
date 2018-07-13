x=int(input("enter the num"))
y=[int(i) for i in input().split()]
min=y[0]
for j in range(0,x):
	if y[j]<min:
		min=y[j]
print(min)
