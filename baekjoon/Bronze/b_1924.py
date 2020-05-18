#요일 구하기
ix,iy=input().split()
x=int(ix)
y=int(iy)
day=0

for i in range(1,x):
    if i in [1,3,5,7,8,10,12]:
        day=day+31
    elif i in [4,6,9,11]:
        day=day+30
    else:
        day=day+28
day=day+y
mday=day%7
if mday==1:
    print("MON")
elif mday==2:
    print("TUE")
elif mday==3:
    print("WED")
elif mday==4:
    print("THU")
elif mday==5:
    print("FRI")
elif mday==6:
    print("SAT")
elif mday==0:
    print("SUN")
