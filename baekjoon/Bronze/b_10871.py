#첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
#둘째 줄에 수열 A를 이루는 정수 N개가 주어진다.
import sys
n,x=input().split()
n=int(n)
x=int(x)

nlist=sys.stdin.readline().split()
ylist=[]

for i in nlist:
    if int(i)<x:
        ylist.append(i)
for i in ylist:
    sys.stdout.write(i+" ")

 
