#그림 그리는 버튼
#사각형 그리기, 타원그리기, 직선 그리기, 삭제
from tkinter import *

window = Tk()
window.title("4번.그림 그리기")
#window.geometry("300x200+100+100")

def drawRect():
    rect = canvas.create_polygon(110,110,180,110,180,180,110,180,fill="white")
def drawLine():
    line = canvas.create_line(50, 50, 200, 200)
def drawOval():
    oval = canvas.create_oval(100,100,150,150)
def clearCanvas():
    canvas.delete(ALL)

frame1 = Frame(window)
frame2 = Frame(window)
frame1.pack(side="top",expand=True)
frame2.pack(side="bottom",expand=True)
#frame1
canvas = Canvas(frame1,relief="solid",bd=2)
canvas.pack()
#frame2
btn1 = Button(frame2,text="사각형",command=drawRect)
btn2 = Button(frame2,text="타원",command=drawOval)
btn3 = Button(frame2,text="직선",command=drawLine)
btn4 = Button(frame2,text="삭제",command=clearCanvas)
btn1.pack(side="left",padx=3)
btn2.pack(side="left",padx=3)
btn3.pack(side="left",padx=3)
btn4.pack(side="left",padx=3)


window.mainloop()

