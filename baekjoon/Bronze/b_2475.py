x=input().split()
a=[]
for i in x:
    a.append(int(i))
y=0
for i in range(0,len(a)):
    y=y+a[i]**2
y=y%10
print(y)
