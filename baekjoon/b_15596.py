#정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.
def solution(a):
    sum=0
    for i in a:
        sum+=i
    return sum

a=[1,2,3,4,5]
print(solution(a))