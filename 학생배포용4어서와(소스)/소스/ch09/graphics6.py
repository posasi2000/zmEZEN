from tkinter import *

window = Tk()
w = Canvas(window, width=300, height=200)
w.pack()
color=colorchooser.askcolor()

w.create_rectangle(50, 25, 200, 100, fill=color[1])
window.mainloop()
