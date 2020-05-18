#num=input('수를 입력하시오:') 입력받으면 문자열인가
#num=5라고 하면 에러 안난다. 
num=int(input('수를 입력하시오:'))
#input은 기본적으로 문자로 입력받는 함수인듯.

if (num%2)==0:
     print('짝수')

else:
     print('홀수')
