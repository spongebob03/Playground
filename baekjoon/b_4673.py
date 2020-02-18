#셀프넘버 아닌 수
def d(n):
    n=str(n)
    a1=int(n)
    sum=0
    for i in n:
        sum+=int(i)
    sum+=a1
    return sum

#1~10000
number_set=[x for x in range(1,10001)]
non=[]
for i in range(1,10001):
    non.append(d(i))
s_non=set(non)
#1~10000에서 셀프넘버 찾기
result=[s for s in number_set if s not in non]
for s in result:
    print(s)