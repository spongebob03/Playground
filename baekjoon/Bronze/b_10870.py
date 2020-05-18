#재귀함수 피보나치
def fiv(n):
    if n==0 or n==1:
        return n
    else:
        return fiv(n-1)+fiv(n-2)
n=int(input())
print(fiv(n))