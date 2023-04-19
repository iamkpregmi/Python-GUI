# Importing Tkinter module
from tkinter import *
from tkinter.ttk import *

# Creating master Tkinter window
master = Tk()

#Title of the GUI application
master.title("Welcome to the GUI App")

#Window Side
master.geometry("500x500")

# Creating object of photoimage class
# Image should be in the same folder
# in which script is saved
p1 = PhotoImage(file = 'info.png')

# Setting icon of master window
master.iconphoto(False, p1)

# Creating Label
Label(master, text="Hello World!").grid(row=0)

# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
mainloop()
