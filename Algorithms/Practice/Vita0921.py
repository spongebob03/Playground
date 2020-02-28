import math
#1. 두 점 사이 거리 구하기
def dist(a,b):
    d=math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)
    return round(d,3)
n=int(input())
s=[]
d=[]
for i in range(n):
    xy=list(map(int,input().split()))
    s.append(xy)
#서로 떨어진 거리 구하기
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        d.append(dist(s[i],s[j]))
print(d)


