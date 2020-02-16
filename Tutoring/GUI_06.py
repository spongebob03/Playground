# 마우스로 사각형 크기 변경 프로그램
from tkinter import *

#왼쪽 버튼->크기 증가
def incRect(event):
    global size
    canvas.delete(ALL)
    size+=10
    canvas.create_rectangle(100,100,100+size,100+size)
def decRect(event):
    global size
    canvas.delete(ALL)
    size-=10
    canvas.create_rectangle(100,100,100+size,100+size)

#윈도우 생성
window = Tk()
window.title("6. Change Rect")
window.geometry("300x300+100+100")

canvas = Canvas(window)
canvas.pack()
size = 100
#사각형 그리기(좌하단, 우상단)
canvas.create_rectangle(100,100,100+size,100+size)

#마우스버튼
canvas.bind("<Button-1>",incRect)
canvas.bind("<Button-3>",decRect)

window.mainloop()

