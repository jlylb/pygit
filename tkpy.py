#!/usr/bin/python
# _*_ coding=utf-8 _*_
import Tkinter
import tkMessageBox
top = Tkinter.Tk()
def helloCallBack():
    tkMessageBox.showinfo("hello python", "hello world")
btn = Tkinter.Button(top, text = "hello,python啊", command = helloCallBack)
btn.pack()
can = Tkinter.Canvas( top,bg = "blue", height = 250,width =300 )
coord = 10, 50, 240, 210
arc = can.create_arc(coord, start=0, extent=150, fill="red")
line = can.create_line(50, 50, 100, 200, fill="green")
can.pack()
chk1 = Tkinter.Checkbutton(top, text = "music", variable = "chkvar1",\
                           onvalue=1, offvalue=0, height=5, width=20
                           )

chk2 = Tkinter.Checkbutton(top, text = "video", variable = "chkvar2",\
                           onvalue=1, offvalue=0, height=5, width=20
                           )
chk1.pack()
chk2.pack()
top.mainloop()
