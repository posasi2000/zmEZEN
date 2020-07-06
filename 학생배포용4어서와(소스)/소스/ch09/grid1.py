from tkinter import *

window = Tk()

b1 = Button(window, text="One")
b2 = Button(window, text="Two")

b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

l = Label(window, text="이것은 레이블입니다.")
l.grid(row=1,column=0)

window.mainloop()
