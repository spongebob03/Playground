#암호해독
import sys

n=int(input())
code=sys.stdin.readline().split()
decode=sys.stdin.readline()
nlist=list()
for i in decode:
    if(i!="\n"):
        nlist.append(i)
#print(nlist)

d=dict()
d[0]=' '
#A-Z
for i in range(1,26+1):
    d[i]=chr(ord('A')+i-1)
#a-z
for i in range(27,52+1):
    d[i]=chr(ord('a')+i-27)

for x in code:
    x=int(x)
    if d[x] in nlist:
        nlist.remove(d[x])

if(len(nlist)==0):
    print("y")
else:
    print("n")
