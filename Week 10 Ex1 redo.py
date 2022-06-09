# User tkinter to create a GUI window
# Title bar should say “RED APPLICATION”
# Dimensions of the window are 400x400
# Make the background of the window red

import tkinter

root = tkinter.Tk()
root.title("RED APPLICATION")
root.geometry("400x400")
root.configure(bg = "red")

root.mainloop()