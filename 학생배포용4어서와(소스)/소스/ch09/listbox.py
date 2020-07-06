from tkinter import *

window = Tk()

lb = Listbox(window, height=4)
lb.pack()
lb.insert(END,"Python")
lb.insert(END,"C")
lb.insert(END,"Java")
lb.insert(END,"Swift")
