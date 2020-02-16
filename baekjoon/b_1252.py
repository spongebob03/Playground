import sys

x=sys.stdin.readline().split()

x1='0b'+x[0]
x2='0b'+x[1]

x1=int(x1,2)
x2=int(x2,2)

y=format(x1+x2,'b')
print(y)




