
result='' #결과 출력할 문자열 

n=int(input())

for i in range(0,n):
     sum=0
     num=input()
     num=num.split()

     a=int(num[0])
     b=int(num[1])
     sum=a+b 
     result = result+str(sum)+'\n'
     #더한 값 문자로 바꿔서 저장하고 반복 

print(result)

