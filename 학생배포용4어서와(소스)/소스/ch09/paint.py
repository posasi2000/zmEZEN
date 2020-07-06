from tkinter import *

w = 500
h = 300

def drawDot( event ):
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   canvas.create_oval( x1, y1, x2, y2, fill = "red" )

window = Tk()
canvas  = Canvas(window, width=w, height=h)
canvas.pack(expand = YES, fill = BOTH)
canvas.bind( "<B1-Motion>", drawDot )

message = Label( window, text = "마우스를 드래그하면 점들이 그려집니다." )
message.pack( side = BOTTOM )
    
mainloop()
