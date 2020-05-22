x=input().split()
xlist=[]
for i in x:
    xlist.append(int(i))
w=xlist[2]-xlist[0]
h=xlist[3]-xlist[1]
if w>xlist[0]:
    w=xlist[0]
if h>xlist[1]:
    h=xlist[1]
if w>h:
    print(h)
else:
    print(w)
