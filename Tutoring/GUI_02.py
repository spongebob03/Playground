#섭씨 화씨 변환
from tkinter import *

def convert():
    temperature = float(temp.get())
    mytemp = (temperature-32)*5/9
    result.config(text=str(mytemp))

window = Tk()
window.title("test")
window.geometry("300x200+100+100")#주의: x소문자...

label = Label(window,text="온도 변환 프로그램")
label.pack()

label2 = Label(window,text="화씨 온도를 입력하시오")
label2.pack(side=TOP,fill=X,padx=5,pady=5,expand=YES)

mytemp = str()
temp = Entry(window,textvariable=mytemp)
temp.pack()

result = Label(window,text="")
result.pack()

btn = Button(window, text='온도 변환!',command=convert,bg='green')
btn.pack()

window.mainloop()