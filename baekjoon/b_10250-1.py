import sys

t=int(input())
for tc in range(0,t):
    x=sys.stdin.readline().split()
    #h층 w방 
    h=int(x[0])
    w=int(x[1])
    n=int(x[2])
    #층inH,호수inW 구하기
    inW=n//h+1
    inH=n%h
    if(inW==0):
        inH=h
        inW+=-1  
    if(inW<10):
        strW="0"+str(inW)
    s=str(inH)+strW
    print(s)
        
