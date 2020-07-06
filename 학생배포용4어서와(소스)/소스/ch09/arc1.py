from tkinter import *

window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()
for degree in range(0, 360, 30):
	canvas.create_arc(10, 10+degree//5, 200, 150+degree//5, extent=degree, style=ARC)
window.mainloop()
