#실행안됨
#실행안됨
from tkinter import *
window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()

id=canvas.create_oval(10, 100, 50, 150, fill="green")

def move_right(event):
    canvas.move(id, 5, 0)
canvas.bind_all('<KeyPress-Right>', move_right)



