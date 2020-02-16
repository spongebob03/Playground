<<<<<<< HEAD
x = int(input())
r=0#5kg
t=0#3kg
if(x%5>=3):
     r=x//5
     t=(x%5)//3
     if(x==(5*r+3*t)):
          print(r+t)
     else:
          if(x%3==0):
               t=x//3
               print(t)
          else:
               print(-1)
else:
     r=(x//5)-1
     t=(x-r*5)//3
     if(x==(5*r+3*t)):
          print(r+t)
     else:
          print(-1)

=======
#1.가장 적은 갯수의 봉지 사용
#2. 1의 경우 만족할 수 없을때, 큰 용량의 봉지를 하나씩 빼고
#작은 봉지로 바꿀 수 있는지. 무작정 큰 봉투만 쓰다가 용량 못맞춤
#3. 1,2경우 써도 해결할 수 없으면 배달 불가

n=int(input())
r=n//5
t=1

if(n%5==0):
    print(r)
else:
    while r>=0:
        t=(n-5*r)//3
        if(n==(5*r+3*t)):
            break
        else:
            r=r-1
    if(r<0):
        print(-1)
    else:
        print(r+t)
    
        
>>>>>>> 069b9c62c4ef3b5a686754b6833aa29f7d63d1a6
