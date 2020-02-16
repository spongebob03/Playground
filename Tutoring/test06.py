import turtle
import random
def calcArea(radius=5):
    return 3.141592*radius**2

def getRange(low,high):
    while True:
        x=int(input("시간을 입력하시오 : "))
        if(x >=low and x<=high):
            print("OK")
            #break or return
            return x
#직선
def drawLine(x1,y1,x2,y2):
    t=turtle.Turtle()
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)

#사각형
def drawRect(x,y,w,h):
    t=turtle.Turtle()
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x+w,y)
    t.goto(x+w,y+h)
    t.goto(x,y+h)
    t.goto(x,y)

def countUP(num1,num2):
    for i in range(num1+1,num2):
        print(i)

print(calcArea())
print(calcArea(4))
#getRange(0,23)
#drawLine(10,20,100,100)
#drawRect(50,50,40,60)
countUP(1,5)
alist=[1,2,3,4,5]

#주사위 확률
diceNum=[0 for i in range(6)]
print(diceNum)
for i in range(1000):
    rd=random.randint(1,6)#1~6
    diceNum[rd-1]+=1
print(diceNum)
for i in range(6):
    print("1000번 중 %d가 나온 횟수 : %d번, 확률 : %.2f%%이다."%(i+1,diceNum[i],diceNum[i]/10))

