import sys
c=int(sys.stdin.readline())

for n in range(0,c):
    x=sys.stdin.readline()
    sum=0
    d=0
    for i in x:
        if(i=='O'):
            d+=1
        else:
            d=0
        sum=sum+d
    print(sum)

