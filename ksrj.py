x=input()
y=input()
if x.isalpha() or y.isalpha():
    print("Invaild")
else:
    x=int(x)
    y=int(y)
    for i in range((x+1),y):
        if i%2!=0:
            print(i,end=' ')
