m=int(input())
n=input().split()
x=[]
for i in n:
    x.append(int(i))
max=x[0]
min=x[0]
for i in range(0,len(x)):
    if max<x[i]:
        max=x[i]
    elif min>x[i]:
        min=x[i]
#res=str(min)+" "+str(max)
print(min,max)