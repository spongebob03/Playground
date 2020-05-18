import sys

x=sys.stdin.readline().split()
m=int(x[0])
n=int(x[1])

for i in range(m,n+1):
     count=0
     for j in range(1,i+1):
          if(i%j==0):
               count+=1
     if(count==2):
          print(i)
