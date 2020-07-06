from tkinter import *
window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()
canvas.create_text(100, 100, text='싱 스트리트(Sing Street)')
mainloop()
