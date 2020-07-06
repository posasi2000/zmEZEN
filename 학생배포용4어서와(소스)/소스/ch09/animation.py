import time
from tkinter import *
window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()
id=canvas.create_oval(10, 100, 50, 150, fill="green")

for i in range(100):
   canvas.move(id, 3, 0)
   window.update()
   time.sleep(0.05)
