#상관계수
import math
def Mean(list):#평균
    return sum(list)/len(list)
def SD(list):#표준편차(소수점 세째자리까지)
    mean=Mean(list)
    sig=0
    for i in list:#편차제곱들의 합
        sig+=(i-mean)**2
    return round(math.sqrt(sig/(len(list)-1)),3)
def z_score(list):#표준점수
    m = Mean(list)
    s=SD(list)
    z=[]
    for i in list:
        z.append((i-m)/s)
    print(z)
    return z
def Corr(data1,data2):#ZSCORE를 사용한 상관계수
    Zx=z_score(data1)
    Zy=z_score(data2)
    n=len(data1)
    sig=0
    for i in range(0,len(data1)):
        sig+=Zx[i]*Zy[i]
    return sig/n
#공분산
def Cov(data1,data2):
    #sig=0
    sumX=0
    sumY=0
    sumXY=0
    n=len(data1)#(x,y)이렇게 1개니까
    for i in range(0,len(data1)):
        #sig+=(data1[i]-Mean(data1))*(data2[i]-Mean(data2))
        sumX+=data1[i]
        sumY+=data2[i]
        sumXY+=data1[i]*data2[i]
    #return sig/(len(data1)+len(data2)-1)
    print("sumX",sumX,"sumY",sumY,"sumXY",sumXY)
    return round((sumXY-sumX*sumY/n)/(n-1),3)

#공분산을 이용한 상관계수
def Corr2(data1,data2):
    cov=Cov(data1,data2)
    print(cov)
    Sx=SD(data1)
    print("Sx=",Sx)
    Sy=SD(data2)
    print("Sy=",Sy)
    return round(cov/(Sx*Sy),3)


#x=input("자료 입력하시오:").split()
#X=[float(i) for i in x]
#y=input("자료 입력하시오:").split()
#Y=[float(i) for i in y]
X=[1,2,2,3,4,5,6,8,9,10]
Y=[2,3,2,5,5,7,5,6,7,8]
#공분산을 이용한 상관계수
print("공분산을 이용한 상관계수",Corr2(X,Y))

print("ZSCORE이용한 상관계수",Corr(X,Y))

#입력 예시
#5 7 8 6 6 10
#2 4 7 2 3 6

#1 2 2 3 4 5 6 8 9 10
#2 3 2 5 5 7 5 6 7 8