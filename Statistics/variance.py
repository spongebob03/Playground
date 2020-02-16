#심리통계 적용 코드
import math
x=input("자료 입력하시오:").split()
data=[float(i) for i in x]

#print(sum(x))
#중앙값 구하는 함수
def Median(list):
    if len(list)%2==0:
        m_idx=int(len(list)/2)
        m=(list[m_idx]+list[m_idx+1])/2
    else:
        m_idx = len(list) // 2
        m=list[m_idx]
    return m
#평균값 구하는 함수
def Mean(list):
    return sum(list)/len(list)

#분산 구하는 함수
def Variance(list):
    m=Mean(list)
    sig=0
    for i in list:
        sig+=(i-m)**2
    return sig/(len(list)-1)
#표준편차 구하는 함수
def SD(list):
    return math.sqrt(Variance(list))
#표준점수(Z score) 구하는 함수
def Zscore(m,s,list):#평균, 표준편차, 데이터 인자로 받는다
    #s=SD(list)
    #m=Mean(list)
    zscore=[]
    for i in list:
        z=(i-m)/s
        zscore.append(z)
    return zscore

# print("중앙값: ",Median(data))
# print("평균: ",Mean(data))
# print("분산: ",Variance(data))
# print("표준편차: ",SD(data))
print("표준점수: ",Zscore(79,12,data))