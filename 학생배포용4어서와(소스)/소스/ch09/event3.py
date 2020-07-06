from tkinter import *

def motion(event):
  print("마우스 위치: (%s %s)" % (event.x, event.y))
  return

window = Tk()
message = """당신 스스로가 하지 않으면
아무도 당신의 운명을 
개선시켜주지 않을 것이다. """

msg = Message(window, text = message)
msg.config(bg='yellow',fg='blue',  font="times 20 italic")
msg.bind('<Motion>',motion)

msg.pack()

window.mainloop()
