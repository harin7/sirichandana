import statistics
z=int(input())
y=input()
y=[int(i) for i in y.split()]
x=statistics.median(y)
print(x)
