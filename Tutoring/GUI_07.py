# 사각형 상하좌우 이동 (grid배치 사용)
from tkinter import *

def moveUp():
    canvas.move(rect,0,-5)
def moveDown():
    canvas.move(rect,0,5)
def moveRight():
    canvas.move(rect,5,0)
def moveLeft():
    canvas.move(rect,-5,0)

window = Tk()
window.title("7.사각형 이동")

canvas = Canvas(window,relief="solid",bd=2)
btn1 = Button(window,text="up",command=moveUp)
btn2 = Button(window,text="down",command=moveDown)
btn3 = Button(window,text="right",command=moveRight)
btn4 = Button(window,text="left",command=moveLeft)

canvas.grid(row=0,column=0,columnspan=4)
btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
btn4.grid(row=1,column=3)

rect = canvas.create_rectangle(100,100,200,200)

window.mainloop()