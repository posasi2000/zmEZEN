from tkinter import *

window = Tk()
colors = ['green', 'red', 'orange','white','yellow','blue']

r = 0
for c in colors:
    Label(window, text=c, relief=RIDGE, width=15).grid(row=r, column=0)
    Button(window, bg=c, width=10).grid(row=r, column=1)
    r = r + 1

window.mainloop()
