from tkinter import *

window = Tk()
photo = PhotoImage(file=".\\ch09\\a1.gif")
w = Label(window, image=photo)
w.photo = photo
w.pack()
window.mainloop()
