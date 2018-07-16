v=input()
v=int(v)
u = []
for i in range(0,v):
    w=input()
    u.append(w)
prefix_len = len(u[0])
for x in u[1 : ]:
    prefix_len = min(prefix_len, len(x))
    while not x.startswith(u[0][ : prefix_len]):
        prefix_len-= 1

prefix = u[0][ : prefix_len]
print (prefix)
