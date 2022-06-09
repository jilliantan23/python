# Create a GUI window with the title “Random”
# Make a yellow button that randomly flips a coin and prints the result
# Make a medium spring green button that randomly rolls a die and prints the result

import random, tkinter

def roll():
    num = random.randrange(1, 7)
    # Create a file
    print(num)
    
def flip():
    num = random.randrange(1, 3)
        # Heads = 1, Tails = 2
    if num == 1: 
        print("Heads!")
    else:
        print("Tails!")

root = tkinter.Tk()
root.title("Random")
root.geometry("400x400")

flip_button = tkinter.Button(root, text = "Flip coin", command = flip)
flip_button.configure(bg = "yellow")
flip_button.grid(row = 0, column = 0)
flip_button.pack()

roll_button = tkinter.Button(root, text = "Roll die", command = roll)
roll_button.configure(bg = "medium spring green")
roll_button.grid(row = 1, column = 0)
roll_button.pack()
    
root.mainloop()