#3. 진약수의 합 
n=int(input())

string="1"
sum=1
for i in range(2,n):
    if(n%i==0):
        string+="+"+str(i)
        sum+=i

print(string+"="+str(sum))
