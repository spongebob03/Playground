#대학 새내기들에게 슬픈 진실을 알려줘야 한다.
import sys

c=int(input())#testcase
lines=0
while(lines<c):
    x=sys.stdin.readline().split()
    n=int(x[0])
    sum=0
    avg=1
    for i in x[1:]:
        sum=sum+int(i)
    avg=sum/n
    #print("testcase: %d n=%d avg=%f"%(lines,n,avg))

    #평균 넘는 학생 수 a
    a=0
    for i in x[1:]:
        if(int(i)>avg):
            a+=1
    
    print("{0:0.3f}%".format(round(a/n*100,6)))
    lines+=1
