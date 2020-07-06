from tkinter import *

window = Tk()

w = Canvas(window, width=300, height=200)
w.pack()

w.create_rectangle(50, 25, 200, 100, fill="blue")
w.create_line(0, 0, 300, 200)
w.create_line(0, 0, 300, 100, fill="red")

mainloop()
