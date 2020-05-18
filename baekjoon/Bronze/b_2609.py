#최대공약수 최소공배수
import sys
x=sys.stdin.readline().split()
x1=int(x[0])
x2=int(x[1])
tmp=0
if(x1<x2):
    tmp=x2
    x2=x1
    x1=tmp
y1=0
y2=0

for i in range(1,x2+1):
    if(x1%i==0 and x2%i==0):
        y1=i
m=x1*x2
for i in range(x2,m+1):
    if(i%x1==0 and i%x2==0):
        y2=i
        break
print(y1)
print(y2)
        
