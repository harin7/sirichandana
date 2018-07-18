x,y=input().split()
a=[]
z=int(len(x))
t=z-int(y)
min=0
k=0
for j in range(0,int(y)):
    c=0
    for i in range(g,z):
        c=c*10+int(x[i])
        if len(str(c))==t:
            a.append(c)
    k=k+1

min=a[0]
for i in a:
    if i<min:
        min=i
print(min)
