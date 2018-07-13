x=int(input())
y=input()
y=[int(i) for i in y.split()]
y.sort()
for i in range (0,x):
    print(y[i],end=" ")
