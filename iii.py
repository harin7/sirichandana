s=input()
t=input()
if s.isalpha() or t.isalpha():
    print(" it is Invaild")
else:
    s=int(s)
    t=int(t)
    for i in range((s+1),t):
        if i%2!=0:
            print(i,end=' ')
