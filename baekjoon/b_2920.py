#1-8 -> ascending, 8-1 -> descending , else: mixed
import sys

x=sys.stdin.readline().split()

asum=0
dsum=0
for i in range(0,8):
    if(int(x[i])==i+1):
        asum+=1
    elif(int(x[i])==8-i):
        dsum+=1
if asum==8:
    print("ascending")
elif dsum==8:
    print("descending")
else:
    print("mixed")
