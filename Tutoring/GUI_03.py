#인치를 센티미터로 변환하는 프로그램. 라벨4개, 버튼1개 엔트리 1개
from tkinter import *

#윈도우 창 설정
window = Tk()
window.title("GUI test")
window.geometry("300x200+100+100")
lab1 = Label(window,text="인치 -> 센티미터")
lab1.pack()

#변환 함수. 버튼 클릭 시 동작
def convert():
    inch = float(input.get())
    x = inch*2.54
    result.config(text=x)

x=str()
input = Entry(window,textvariable=x)
input.pack()
button = Button(window,text="convert!",command=convert)
button.pack()

result=Label(window,text="")
result.pack()

window.mainloop()