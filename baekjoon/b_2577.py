import sys
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())
mul=a*b*c
strm=str(mul)
num=['0','1','2','3','4','5','6','7','8','9']
count=[0,0,0,0,0,0,0,0,0,0]
#print(mul)

for i in strm:
    for n in range(0,10):
        if(i==num[n]):
            count[n]+=1
            
for i in count:
    print(i)
