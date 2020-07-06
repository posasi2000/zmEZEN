#에러 from Tkinter import *
from tkinter import *

window = Tk()

Label(window, text="박스 #1", bg="red", fg="white").pack()
Label(window, text="박스 #2", bg="green", fg="black").pack()
Label(window, text="박스 #3", bg="blue", fg="white").pack()

mainloop()
