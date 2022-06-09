# Create a search GUI with a "Search" label, an Entry box, and a "Submit" button in one row
# When the submit button is pressed, search for the text in the Entry box inside of sport_news.txt
# Show a messagebox stating if the text was found or not
# If the text was found, clear out the Entry box to prepare for the next search

import tkinter, tkinter.messagebox

def search():
    """Searches to see if a search string is in side of sports_news.txt."""
    global search_box
    
    with open("sport_news.txt", "r") as file:
        file_contents = file.read()
    # if searching for numbers must convert to string for get() method
    if search_box.get().lower().strip() in file_contents.lower().strip():
        # refers to enter text box, only what user typed into the box using .get()
        tkinter.messagebox.showinfo("Success!", "Your search was found.")
    else:
        tkinter.messagebox.showwarning("Failure!", "Your search was not found.")
        
    search_box.delete(0, tkinter.END)
    
root = tkinter.Tk()
root.title("Search sports_news.txt")

search_label = tkinter.Label(root, text = "Search:")
search_label.grid(row = 0, column = 0)

search_box = tkinter.Entry(root, width = 10)
search_box.grid(row = 0, column = 1)


search_button = tkinter.Button(root, text = "Submit", command = search)
search_button.grid(row = 0, column = 2)


root.mainloop()
