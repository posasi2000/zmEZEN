from tkinter import *

window = Tk()

canvas = Canvas(window,  width=300, height=200)
canvas.pack()

img = PhotoImage(file=".\\ch09\\starship.png")
canvas.create_image(20, 20, anchor=NW, image=img)

mainloop()
