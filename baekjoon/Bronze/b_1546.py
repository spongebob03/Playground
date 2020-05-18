import sys

n=int(input())

x=sys.stdin.readline().split()
nlist=[]
m=0

for i in x:
    if(m<int(i)):
        m=int(i)      
for i in x:
    nlist.append(int(i)/m*100)
sum=0
for i in nlist:
    sum=sum+i
print(float(sum/n))
