from tkinter import *

gui = Tk(className='Python Examples - Window Size')
# set window size
gui.geometry("500x200")

a = Label(gui, text ="Hello World")
a.pack()

gui.mainloop() 
