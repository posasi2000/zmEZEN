from tkinter import *
window = Tk()

canvas = Canvas(window, width=300, height=200)
canvas.pack()

canvas.create_polygon(10, 10, 150, 110, 250, 20, fill="blue")
window.mainloop()
