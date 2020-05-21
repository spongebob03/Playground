xlist=[]
for i in range(0,9):
    x=int(input())
    xlist.append(x)
m=max(xlist)
print(m)
for i in range(0,9):
    if(m==xlist[i]):
        print(i+1)
