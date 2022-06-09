# Create a GUI with a combobox that has options for English, French, and Spanish
# When a button is pressed, show a messagebox with a matching greeting
# English -> Hello; French -> Bonjour; Spanish -> Hola

import tkinter, tkinter.messagebox, tkinter.ttk

def greeting_msg():
    """Shows an appropriate messagebox on the appropriate language."""
    global language_box 
    if language_box.get() == "English":
        tkinter.messagebox.showinfo("Greeting", "Hello")
    elif language_box.get() == "French":
        tkinter.messagebox.showinfo("Greeting", "Bonjour")
    else:
        tkinter.messagebox.showinfo("Greeting", "Hola")
root = tkinter.Tk()
root.title("International greetings")

language_box = tkinter.ttk.Combobox(root, values = ["English", "French", "Spanish"], state = "readonly")
language_box.current(0) # Makes first element as the default option
language_box.grid(row = 0, column = 0)

greet_button = tkinter.Button(root, text = "Greet!", command = greeting_msg)
greet_button.grid(row = 0, column = 1)

root.mainloop()