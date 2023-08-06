import tkinter

master = tkinter.Tk()
master.title("Input Field")
master.geometry("500x500")

tkinter.Label(master, text="First Name: ").grid(row=0)
# e1 = tkinter.Entry(master)
# e1.grid(row=0, column=1)
tkinter.Entry(master).grid(row=0, column=1)
tkinter.Label(master, text="Last Name: ").grid(row=1)
tkinter.Entry(master).grid(row=1,column=1)

master.mainloop()