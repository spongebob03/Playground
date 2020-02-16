#글자 수평으로 이동하는 애니메이션
from tkinter import *
import time

window = Tk()
window.title("5번 글자이동")
#window.geometry("300x100+100+100")

canvas = Canvas(window, bg="white",width =300, height=200)
canvas.pack()

text = canvas.create_text(10,50,text="welcom to Python Cafe")

#캔버스 업데이트 이용해 움직이는 것처럼
while True:
    canvas.move(text, 2, 0)
    window.update()
    time.sleep(0.05)

window.mainloop()