#ACM호텔 문제
t=int(input())
for i in range (0,t):
    x=input().split()

    h=int(x[0])
    w=int(x[1])
    n=int(x[2])
    r1=n%h
    r2=n//h+1
    res=str(r1)
    sr2=str(r2)
    if r2<10:
        sr2="0"+sr2

    print(res+sr2)

