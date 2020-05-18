import sys

t=int(input())
for tc in range(0,t):
    x=sys.stdin.readline().split()
    #h층 w방 
    h=int(x[0])
    w=int(x[1])
    acm=list()
    hlist=list()

    for i in range(1,h+1):
        strh=str(i)
        for j in range(1,w+1):
            strw=str(j)
            if(j<10):
                strw="0"+str(j)
            acm.append(strh+strw)

    for i in range(0,h):
        hlist.append(acm[w*i:w*(i+1)])

    #n번째 손님
    n=int(x[2])
    idxW=n//h
    idxH=n%h-1
    if(idxH==0):
        idxH=h-1
    room=hlist[idxH][idxW]
    print(room)
