from tkinter import *

window = Tk()
window.title("1.정보입력")

def show():
    print("이름 : ",str(entry1.get()))
    print("직업 : ",str(entry2.get()))
    print("국적 : ",str(entry3.get()))

label1=Label(window,text="이름")
label2=Label(window,text="직업")
label3=Label(window,text="국적")
btn1=Button(window,text="Show",command=show)
btn2=Button(window,text="Quit",command=window.quit)
entry1 = Entry(window)
entry2 = Entry(window)
entry3 = Entry(window)

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
entry1.grid(row=0,column=1,columnspan=4)
entry2.grid(row=1,column=1,columnspan=4)
entry3.grid(row=2,column=1,columnspan=4)
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1,sticky="w")

window.mainloop()

