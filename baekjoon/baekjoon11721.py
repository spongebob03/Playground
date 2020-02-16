#한 줄에 10글자씩 끊어서 출력

string=input() #문자열 입력받아서
n=len(string)  #문자열 길이

for i in range(0,n//10+1):#한줄에 10글자씩 끊어서
     print(string[10*i:10*(i+1)])#0:10,10:20..
     i +=1
     
