#두번째로 큰 정수 출력
nums=input()
nums=nums.split()

a=int(nums[0])
b=int(nums[1])
c=int(nums[2])
mid=0

if (a>b and a>c):
     if b>=c:
          mid=b
     else:
          mid=c
elif (b>a and b>c):
     if a>=c:
          mid=a
     else:
          mid=c
elif (c>a and c>b):
     if a>=b:
          mid=a
     else:
          mid=b
print(mid)
