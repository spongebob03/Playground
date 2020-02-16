#20판 했을때 결과 점수
import sys

def score(w,l,d):
    r=20*w*50+20*l*(-50)+20*d*0
    return r

x=sys.stdin.readline().split()
w=float(x[0])
l=float(x[1])
d=float(x[2])
print(score(w,l,d))
