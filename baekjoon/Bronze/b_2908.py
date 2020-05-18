import sys

x=sys.stdin.readline().split()

def sangsu(n):
    s=''
    for i in range(len(n)-1,-1,-1):
        s+=n[i]
    s=int(s)
    return s

x1=sangsu(x[0])
x2=sangsu(x[1])

if x1>x2:
    print(x1)
else:
    print(x2)
                        
