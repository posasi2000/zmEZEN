from tkinter import *

window = Tk()

select = IntVar()
select.set(1)  

list = [ ("Python",1),    ("C",2),    ("Java",3),    ("Swift",4), ]

def PrintChoice():
    print( select.get())

Label(window, 
     text="가장 선호하는 프로그래밍 언어를 선택하시오",
      justify = LEFT,
      padx = 20).pack()

for txt, val in list:
    Radiobutton(window, 
                text=txt,
                padx = 20, 
                variable=select, 
                command=PrintChoice,
                value=val).pack(anchor=W)

mainloop()
