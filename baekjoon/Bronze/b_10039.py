import sys

nlist=[]
for i in range(0,5):
    x=int(sys.stdin.readline())
    if(x<40):
        x=40
    nlist.append(x)

sum=0
for i in nlist:
    sum+=i
print(int(sum/5))
