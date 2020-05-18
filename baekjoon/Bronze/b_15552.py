import sys

n=sys.stdin.readline().rstrip()
n=int(n)
while(n>0):
    x,y=sys.stdin.readline().rstrip().split()
    x=int(x)
    y=int(y)
    print(x+y)
    n=n-1
