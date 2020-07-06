from tkinter import *

window = Tk()

Label(window, 
		 text="Times Font 폰트와 빨강색을 사용합니다.",
		 fg = "red",
		 font = "Times 32 bold italic").pack()
Label(window, 
		 text="Helvetica 폰트와 녹색을 사용합니다.",
		 fg = "blue",
		 bg = "yellow",
		 font = "Helvetica 32 bold italic").pack()
window.mainloop()
