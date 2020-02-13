# !/usr/bin/python3
# ref: https://www.tutorialspoint.com/python3/tk_checkbutton.htm
from tkinter import Tk, IntVar, Checkbutton

import tkinter
    
top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20, )
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.pack()
C2.pack()
top.mainloop()