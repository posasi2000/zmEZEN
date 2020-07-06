from tkinter import *


window = Tk()
f = Frame(window)

b1 = Button(f, text="One")
b2 = Button(f, text="Two")
b3 = Button(f, text="Three")

b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)

l = Label(window, text="이 레이블은 버튼들 위에 배치된다.")
l.pack()
f.pack()

window.mainloop()
