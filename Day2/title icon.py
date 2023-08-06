import tkinter

master = tkinter.Tk()

#Image on top of the window
p1 = tkinter.PhotoImage(file="myimage.png")
master.iconphoto(False,p1)

master.title("Input Field")
master.geometry("500x500")
master.minsize(500,500)
master.maxsize(500,500)

tkinter.Label(master, text="This is the Simple Text").grid(row=0)

master.mainloop()