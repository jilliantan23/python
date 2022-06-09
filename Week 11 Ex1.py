# Create a GUI in light green titled: "Soccer"
# Create labels for "Real Madrid: 3" and "Liverpool: 1"
# Create a button with the text "Click me" that
# opens a popup saying "Real Madrid wins!"

import tkinter, tkinter.messagebox

def show_result():
    """Shows a messagebox with the soccer results."""
    tkinter.messagebox.showinfo("Soccer results", "Real Madrid wins!")
    global root
    root.destroy()
    
root = tkinter.Tk()
root.title("Soccer")
root.configure(bg = "light green")

madrid_label = tkinter.Label(root, text = "Real Madrid: 3")
madrid_label.configure(bg = "light green")
madrid_label.pack()

pool_label = tkinter.Label(root, text = "Liverpool: 1")
pool_label.configure(bg = "light green")
pool_label.pack()

result_button = tkinter.Button(root, text = "Click me", command = show_result)
result_button.pack()

root.mainloop()