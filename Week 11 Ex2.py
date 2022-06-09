# Create labels for hello and goodbye
# Create buttons for hello and goodbye
# When pressed, a messagebox should pop up with the appropriate statement
# Make with light blue background

import tkinter, tkinter.messagebox

def hello_msg():
    """Messagebox to say hello."""
    tkinter.messagebox.showinfo("Hello", "Hello!!!!!!")
    
def goodbye_msg():
    """Messagebox to say goodbye."""
    tkinter.messagebox.showinfo("Goodbye", "Goodbye!!!!")
    
root = tkinter.Tk()
root.title("Hello/goodbye")
root.configure(bg = "light blue")
root.geometry("400x400")

hello_label = tkinter.Label(root, text = "Hello -->")
hello_label.configure(bg = "light blue")
hello_label.grid(row = 0, column = 0, padx = 5, pady = 5)

goodbye_label = tkinter.Label(root,text = "Goodbye -->")
goodbye_label.configure(bg = "light blue")
goodbye_label.grid(row = 1, column = 0, padx = 5, pady = 5)

hello_button = tkinter.Button(root, text = "Click me!", command = hello_msg)
hello_button.grid(row = 0, column = 1, padx = 5, pady = 5)

goodbye_button = tkinter.Button(root, text = "Click me!", command = goodbye_msg)
goodbye_button.grid(row = 1, column = 1, padx = 5, pady = 5)

root.mainloop()