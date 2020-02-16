from tkinter import *

fields = '이름','직업','국적'

def fetch(entries):
    for entry in entries:
        fields = entry[0]
        text = entry[1].get()
        print("%s: %s"%(fields,text))

def makeform(root,fields):
    entries =[]
    for field in fields:
        frame = Frame(root)
        lab = Label(frame, width=15,text=field, anchor='w')
        ent = Entry(frame)

        frame.pack(side=TOP,fill=X,padx=5,pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT,expand=YES,fill=X)

        entries.append((field,ent))
    return entries

window = Tk()
ents = makeform(window,fields)
window.bind('<Return>',(lambda event,e=ents: fetch(e)))
b1 = Button(window, text='Show',command=(lambda e=ents:fetch(e)))
b2 = Button(window, text='Quit', command=window.quit)
b1.pack(side=LEFT,padx=5,pady=5)
b2.pack(side=LEFT,padx=5,pady=5)
window.mainloop()