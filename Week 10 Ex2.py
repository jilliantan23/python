# User tkinter to create a GUI window
# Title bar should say “SDSU Basketball”
# Make the background of the window yellow
# Make labels for “Wins: 23” and “Losses: 5”

import tkinter

root = tkinter.Tk()
root.title("SDSU Basketball")
root.configure(bg = "yellow")

new_label = tkinter.Label(root, text = "Wins: 23")
new_label.pack()
another_label = tkinter.Label(root, text = "Losses: 23")
another_label.pack()

root.mainloop()