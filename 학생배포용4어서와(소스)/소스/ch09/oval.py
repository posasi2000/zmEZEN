from tkinter import *

window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()
canvas.create_oval(10, 10, 200, 150)
window.mainloop()
