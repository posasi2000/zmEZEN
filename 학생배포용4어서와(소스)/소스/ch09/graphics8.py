import random
from tkinter import *

window = Tk()
canvas = Canvas(window, width=500, height=400)
canvas.pack()
color = ["red", "orange", "yellow", "green", "blue", "violet"]

def draw_rect():
    x = random.randint(0, 500)
    y = random.randint(0, 400)
    w = random.randrange(100)
    h = random.randrange(100)
    canvas.create_rectangle(x, y, w, h, fill = random.choice(color))

for i in range(10):
    draw_rect()
    
window.mainloop()
