from tkinter import *

def sleft(event):
    print("단일 클릭, 왼쪽 버튼") 
def dleft(event):                           
    print("더블 클릭, 왼쪽 버튼") 

widget = Button(None, text='마우스 클릭')
widget.pack()

widget.bind('<Button-1>', sleft)
widget.bind('<Double-1>', dleft) 

widget.mainloop()
