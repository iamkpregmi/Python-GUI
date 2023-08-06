from tkinter import *

master = Tk()
master.title("Check Button")
master.geometry("400x400")
var1 = IntVar()
var2 = IntVar()
Checkbutton(master, text="Male", variable=var1).grid(row=0, sticky=W)
Checkbutton(master, text="Female", variable=var2).grid(row=1, sticky=W)

mainloop()