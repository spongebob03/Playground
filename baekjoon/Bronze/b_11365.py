import sys

while(True):
    x=input()
    n=len(x)
    if(x=='END'):
        break
    for i in range(n-1,-1,-1):
        sys.stdout.write(x[i])
    print()


