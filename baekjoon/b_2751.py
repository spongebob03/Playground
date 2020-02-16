#정렬
#시간초과로 뜸;; 어째서?!
import sys

n=int(sys.stdin.readline())
nlist=[]
for i in range(0,n):
    x=int(sys.stdin.readline())
    nlist.append(x)
tmp=0
for j in range(0,n):
    for i in range(0,n-j-1):
        if(nlist[i]>nlist[i+1]):
            tmp=nlist[i]
            nlist[i]=nlist[i+1]
            nlist[i+1]=tmp

for i in nlist:
    print(i)
    
