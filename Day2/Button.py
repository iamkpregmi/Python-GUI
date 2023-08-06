import tkinter

master = tkinter.Tk()
master.title("First Program")
master.geometry("400x400")

button = tkinter.Button(master, text="Close Program", width= 25, command= master.destroy)
button.pack()

master.mainloop()