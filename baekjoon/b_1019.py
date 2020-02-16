n=int(input())

cnt=[0,0,0,0,0,0,0,0,0,0]
for i in range(0,n):
    i=str(i)
    for j in i:
        for num in range(0,10):
            if j==str(num):
                cnt[num]+=1
print(cnt)
            
