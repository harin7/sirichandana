x=input()
y=input()
z=input()
print(greatest number is")
if x<y:
	if y<z:
		print(z)
	else:
		print(y)
elif y<z:
	if z<x:
		print(x)
	else:
		print(z)
elif z<x:
	if x<y:
		print(y)
	else:
		print(x)
