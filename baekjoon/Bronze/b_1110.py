import sys

#x=sys.stdin.readline()
x=input()
if(int(x)<10):
    x="0"+x
initx=x #최초의 수
x1=x[len(x)-2]
x2=x[len(x)-1]

t=0
while(True):
    t+=1
    y=int(x1)+int(x2)
    s=""
    if(y>=10):
        y=str(y)
        s=y[1]
    else:
        y=str(y)
        s=y[0]
    x=x+s
    #print("%d번=>"%t+x)
    x1=x[len(x)-2]
    #print("%d번 x1:"%t+x1)
    x2=x[len(x)-1]
    #print("%d번 x2:"%t+x2)
    
    if(initx==x1+x2):
        break
print(t)
