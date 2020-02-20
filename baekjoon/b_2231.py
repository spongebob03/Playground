#sol1. use str,len
#sol2. use %,/
y=int(input())
a=[]
n=y
d=0

while True:
    a.append(n % 10)
    n=n//10
    d+=1
    if n==0:
        break

def sol(y):
    for x in range(y - 9 * d, y):
        n = x
        a=[]
        while True:
            a.append(n%10)
            n=n//10
            if n==0:
                break
        if x+sum(a) ==y:
            return x
        else:
            return 0

print(sol(y))

