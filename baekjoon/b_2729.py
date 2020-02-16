#이진수 덧셈
import sys

t=int(input())
for i in range(0,t):
    x=sys.stdin.readline().split()
    x1=x[0]
    x2=x[1]

    #정수로 바꿔서 더하고
    x1=int(x1,2)
    x2=int(x2,2)
    y=x1+x2
    #이진수로 바꾼다
    y=bin(y)
    print(y[2:])
