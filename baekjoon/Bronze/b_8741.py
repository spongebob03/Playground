k=int(input())
n=2**k

sum=0
for i in range(0,n):
    sum+=i

#시간초과;; 아니 왜... 
sum=bin(sum)

print(sum[2:])
