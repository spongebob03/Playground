import sys

c=int(sys.stdin.readline())
for n in range(0,c):

    x=sys.stdin.readline().split()
    r=int(x[0])
    s=x[1]

    st=''
    for i in s:
        st+=i*r

    print(st)
