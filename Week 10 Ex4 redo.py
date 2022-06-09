# Allow the user to enter unlimited values
# Use showwarning if they enter a bad value
import tkinter, tkinter.messagebox

repeat = "yes"

while repeat.lower().strip() == "yes":
    try:
        entry = float(input("Enter a number: "))
        tkinter.messagebox.showinfo("Awesome", "Your number was valid.")
    except:
        tkinter.messagebox.showwarning("Warning", "You entered a bad value")
    
    repeat = input("Enter another value (yes/no)? ")