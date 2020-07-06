from tkinter import *
window = Tk()
canvas = Canvas(window, width=500, height=200)
canvas.pack()
canvas.create_text(250, 10, text='Sing Street', fill='blue', font=('Courier', 20))
canvas.create_text(250, 100, text='Sing Street', fill='red', font=('Hevetica', 30))
canvas.create_text(250, 150, text='Sing Street', font=('Times', 40), fill='green')
mainloop()
