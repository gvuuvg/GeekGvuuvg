import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.wm_minsize(400, 160)
sn = tkinter.Entry(root, width=32, justify='right', font=12)
sn.grid(row=0, column=0, columnspan=5)


def show(sne, v):
    """显示符号到显示屏"""
    sne.insert(tkinter.END, v)


def get_clean():
    sn.delete(0, tkinter.END)


def gr():
    """计算结果"""
    # res = eval(sn.get())
    # get_clean()
    # sn.insert(0, str(res))
    try:
        res = round(eval(sn.get()), 2)
    except Exception as e:
        tkinter.messagebox.showinfo("提示", e)
        return
    get_clean()
    sn.insert(0, str(res))
    # try:
    #     res = round(eval(show.get()), 2)
    # except Exception as e:
    #     # 错误提示
    #     tkinter.messagebox.showinfo("提示", e)
    #     return
    # get_clean()
    # show.insert(0, str(res))


n1 = tkinter.Button(root, width=8, text='1', height=2, command=lambda: show(sn, "1"))
n1.grid(row=1, column=0)
n2 = tkinter.Button(root, width=8, text='2', height=2, command=lambda: show(sn, "2"))
n2.grid(row=1, column=1)
n3 = tkinter.Button(root, width=8, text='3', height=2, command=lambda: show(sn, "3"))
n3.grid(row=1, column=2)
n4 = tkinter.Button(root, width=8, text='4', height=2, command=lambda: show(sn, "4"))
n4.grid(row=1, column=3)
n5 = tkinter.Button(root, width=8, text='5', height=2, command=lambda: show(sn, "5"))
n5.grid(row=1, column=4)

n6 = tkinter.Button(root, width=8, text='6', height=2, command=lambda: show(sn, "6"))
n6.grid(row=2, column=0)
n7 = tkinter.Button(root, width=8, text='7', height=2, command=lambda: show(sn, "7"))
n7.grid(row=2, column=1)
n8 = tkinter.Button(root, width=8, text='8', height=2, command=lambda: show(sn, "8"))
n8.grid(row=2, column=2)
n9 = tkinter.Button(root, width=8, text='9', height=2, command=lambda: show(sn, "9"))
n9.grid(row=2, column=3)
n0 = tkinter.Button(root, width=8, text='0', height=2, command=lambda: show(sn, "0"))
n0.grid(row=2, column=4)

np = tkinter.Button(root, width=8, text='+', height=2, command=lambda: show(sn, "+"))
np.grid(row=3, column=0)
nm = tkinter.Button(root, width=8, text='-', height=2, command=lambda: show(sn, "-"))
nm.grid(row=3, column=1)
nu = tkinter.Button(root, width=8, text='*', height=2, command=lambda: show(sn, "*"))
nu.grid(row=3, column=2)
nd = tkinter.Button(root, width=8, text='/', height=2, command=lambda: show(sn, "/"))
nd.grid(row=3, column=3)
nt = tkinter.Button(root, width=8, text='.', height=2, command=lambda: show(sn, "."))
nt.grid(row=3, column=4)

nc = tkinter.Button(root, width=16, text='C', height=2, command=get_clean)
nc.grid(row=4, column=0, columnspan=2)
ne = tkinter.Button(root, width=16, text='=', height=2, command=gr)
ne.grid(row=4, column=2, columnspan=2)

root.mainloop()
