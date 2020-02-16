#심리통계
#z-test

def z_test():
    m = float(input("M:"))
    x = float(input("X:"))
    s = float(input("S:"))
    n = int(input("N:"))
    z=(x-m)/(s/n**0.5)

    return z

#단일표본 T검증
def t_test1(x,m,s,n):
    t=(x-m)/(x/n**0.5)

    return t
#종속표본 T검증
def t_test2():
    x1=float(input("x1:"))
    x2=float(input("x2:"))
    m1=float(input("m1:"))
    m2=float(input("m2:"))
    s=float(input("s:"))
    d=x1-x2

    return 0
#독립표본 T검증
def t_test3():
    x1 = float(input("x1:"))
    x2 = float(input("x2:"))
    m1 = float(input("m1:"))
    m2 = float(input("m2:"))
    s1 = float(input("s1:"))
    s2 = float(input("s2:"))


#아...다음에 하자




