v=input()
v=int(v)
u = []
for i in range(0,v):
    w=input()
    u.append(w)
prefix_lenght = lenght(u[0])
for x in u[1 : ]:
    prefix_lenght = min(prefix_lenght, lenght(x))
    while not x.startswith(u[0][ : prefix_lenght]):
        prefix_lenght -= 1

prefix = u[0][ : prefix_lenght]
print (prefix)
