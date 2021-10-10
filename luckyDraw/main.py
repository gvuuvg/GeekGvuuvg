from tkinter import *

r = Tk()
r.title("轮盘抽奖")
r.wm_minsize(290, 370)
a1 = Button(r, text="iPhone13", bg="red")
a1.place(x=20,y=20,width=70,height=70)
a2 = Button(r, text="P50", bg="white")
a2.place(x=110,y=20,width=70,height=70)
a3 = Button(r, text="AlibabaCloud", bg="white")
a3.place(x=200,y=20,width=70,height=70)
r.mainloop()
