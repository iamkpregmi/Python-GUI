# Import tkinter module
import tkinter as tk

# Create a window
window = tk.Tk()
window.title("Input and Output")

# Create a label to display instructions
label = tk.Label(window, text="Enter some text and click the button")
label.pack()

# Create an entry widget to get input from the user
entry = tk.Entry(window)
entry.pack()

# Create a function to handle the button click
def button_click():
    # Get the input from the entry widget
    input = entry.get()
    # Display the output in a label
    output = tk.Label(window, text="You entered: " + input)
    output.pack()

# Create a button to trigger the function
button = tk.Button(window, text="Click me", command=button_click)
button.pack()

# Start the main loop of the window
window.mainloop()
