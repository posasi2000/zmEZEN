from tkinter import *

window = Tk()

sb = Scrollbar(window, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)

lb = Listbox(window, height=4)
lb.pack()
lb.insert(END,"Python")
lb.insert(END,"C")
lb.insert(END,"Java")
lb.insert(END,"Swift")
lb.insert(END,"Go")
lb.insert(END,"C++")
lb.insert(END,"C#")
