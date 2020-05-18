import sys

t=int(sys.stdin.readline())
for i in range(0,t):
    x=sys.stdin.readline().split()
    x1=int(x[0])
    x2=int(x[1])
    print("Case #%d: %d + %d = %d"%(i+1,x1,x2,x1+x2))

