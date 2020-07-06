from tkinter import *

def show():
   print("이름: %s\n나이: %s" % (e1.get(), e2.get()))
   
parent  = Tk()
Label(parent , text="이름").grid(row=0)
Label(parent, text="나이").grid(row=1)

e1 = Entry(parent)
e2 = Entry(parent)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(parent, text='보이기', command=show).grid(row=3, column=1, sticky=W, pady=4)
Button(parent, text='종료', command=parent.quit).grid(row=3, column=0, sticky=W, pady=4)

mainloop()
