from tkinter import *

window = Tk()

w = Label(window, text="박스 #1", bg="red", fg="white")
w.pack(fill=X)
w = Label(window, text="박스 #2", bg="green", fg="black")
w.pack(fill=X)
w = Label(window, text="박스 #3", bg="blue", fg="white")
w.pack(fill=X)

mainloop()
