#opens the "Random Netflix TV Shows & Movies Search" window
#Choose based on Movie Rating, Show Rating, Release Year, Country of Production, Duration, or random
#Movie Rating picking then click search button
#same for show rating and duration
#same for preferred country of production
#enter release year preference of any movie or show
# years between 1925-2021
#dark blue button combines all searches ?
#green button randomly chooses any movie or show to watch

import tkinter, tkinter.messagebox, random, json, csv
import random as rand

#find a random movie based on movie rating column-8
def movie_rating():
    global root
    with open("netflix_titles.csv", "r") as file:
        reader = csv.reader(file)
        ratings1 = list(reader)
        for line in reader:
            if ratings.get() in line[8]:
                random = random.randrange(line[8])
                movie_rating = tkinter.Toplevel()
                movie_rating = tkinter.messagebox.showinfo("Suggested pick")
                movie_rating.title("Your suggested movie pick is")
                movie_rating.geometry("400x200")
                print("Movie Rating: ", line[8])
        
def show_rating():
    with open("netflix_titles.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            if show_box.get() == line[8]:
                random = random.randrange(line[8])
                show_rating = tkinter.Toplevel()
                show_rating.title("Suggested shows based on rating")
                show_rating.geometry("400x200")
                shows = tkinter.Label(show_rating, text = "List of show suggestions:")
            print("Movie Rating: ", line[3])
                
def release_yr():
    with open("netflix_titles.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            if release.get().lower().strip() == line[7]:
                random = random.randrange(line[7])
                releases = tkinter.Toplevel()
                releases.title("Suggestions based on release year")
                releases.geometry("400x200")
                rel_yr = tkinter.Label(show_rating, text = "List of suggestions:")
            print("Movie Rating: ", line[3])
            
def country():
    with open("netflix_titles.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            if country_search.get() == line[5]:
                random = random.randrange(line[5])
                ctr = tkinter.Toplevel()
                ctr.title("Suggestions based on country of origin")
                ctr.geometry("400x200")
                countries = tkinter.Label(show_rating, text = "List of suggestions:")
            print("Movie Rating: ", line[3])
                
def duration():
    with open("netflix_titles.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            if dur_ation.get() == line[9]:
                random = random.randrange(line[9])
                dur = tkinter.Toplevel()
                dur.title("Suggestions based on country of origin")
                dur.geometry("400x200")
                durations = tkinter.Label(show_rating, text = "List of suggestions:")
            print("Movie Rating: ", line[3])
            
def random_choosing():
    """Randomly chooses a movie/ show for user"""
    # Find a random # of row from "netflix_titles.csv"
    with open("netflix_titles.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            i = random.randrange(3, 100, 2)
            chosen = line[i]
        print(chosen)
    print(chosen) 
    tkinter.messagebox.showinfo("We recommended: ", chosen)
    
def all():
    """Generates random movies and shows for users based on all preferences"""
    all_list = []
    with open("netflix_titles.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            if ratings.get() == line[9]:
                all_list.append(row)
                movie_rating = tkinter.Toplevel()
                movie_rating.title("Your suggested movie pick is")
                movie_rating.geometry("400x200")
    print("All matching movies & shows ", all_list)

root = tkinter.Tk()
root.title("Random Netflix TV Shows & Movies Search")

search_label = tkinter.Label(root, text = "Choose based on ")
search_label.grid(row = 0, column = 0, padx = 5, pady = 5)
search_label.configure(fg = "red")

country_label = tkinter.Label(root, text = "Country of production: ")
country_label.grid(row = 0, column = 5, padx = 5, pady = 5)

country_search = tkinter.ttk.Combobox(root, values = ["Argentina", "Belgium", "Brazil", "Canada", "Chile", "China", "Colombia", "Denmark", "Egypt", "France", "Hong Kong", "India", "Iceland", "Iran", "Israel", "Japan", "Mexico", "Nigeria", "Philippines", "Poland", "Russia", "Singapore", "South Africa", "Spain", "Sweden", "Taiwan", "Turkey", "United Arab Emirates", "United States", "United Kingdom", "Uruguay"], state = "readonly")
country_search.current(0)
country_search.grid(row = 0, column = 6)

typee = tkinter.Label(root, text = "Show Rating ")
typee.grid(row = 1, column = 1, padx = 5, pady = 5)

rating_label = tkinter.Label(root, text = "Movie Rating ")
rating_label.grid(row = 0, column = 1, padx = 5, pady = 5)

ratings = tkinter.ttk.Combobox(root, values = ["G", "PG", "PG-13", "R"], state = "readonly")
ratings.current(0)
ratings.grid(row = 0, column = 2 )

search_button = tkinter.Button(root, text = "Search", command = movie_rating)
search_button.configure(fg = "red")
search_button.grid(row = 0, column = 3, padx = 5, pady = 5)

search_button = tkinter.Button(root, text = "Search", command = show_rating)
search_button.configure(fg = "red")
search_button.grid(row = 1, column = 3, padx = 5, pady = 5)

search_button = tkinter.Button(root, text = "Search", command = country)
search_button.configure(fg = "red")
search_button.grid(row = 0, column = 7, padx = 5, pady = 5)

search_button = tkinter.Button(root, text = "Search", command = duration)
search_button.configure(fg = "red")
search_button.grid(row = 1, column = 7, padx = 5, pady = 5)

search_button = tkinter.Button(root, text = "Search", command = release_yr)
search_button.configure(fg = "red")
search_button.grid(row = 2, column = 3, padx = 5, pady = 5)

show_box = tkinter.ttk.Combobox(root, values = ["TV-G","TV-PG", "TV-14", "TV-MA"], state = "readonly")
show_box.current(0)
show_box.grid(row = 1, column = 2)

duration = tkinter.Label(root, text = "Duration")
duration.grid(row = 1, column = 5, padx = 5, pady = 5)

dur_ation = tkinter.ttk.Combobox(root, values = ["1 Season", "2 Seasons", "3 Seasons", "more than 3 seasons"], state = "readonly")
dur_ation.current(0)
dur_ation.grid(row = 1, column = 6)

release = tkinter.Label(root, text = "Release year (1925-2021)")
release.grid(row = 2, column = 1)

release_note = tkinter.Label(root, text = "Please enter a year between 1925 and 2021")
release_note.grid(row = 3, column = 2)
release_note.configure(fg = "pink")

release_search = tkinter.Entry(root, width = 20)
release_search.grid(row = 2, column = 2, padx = 5, pady = 5)

search_all = tkinter.Button(root, text = "Search using all categories", command = all)
search_all.grid(row = 2, column = 6)
search_all.configure(fg = "light blue")

random = tkinter.Button(root, text = "Randomly Choose for me!", command = random_choosing)
random.grid(row = 3, column = 6)
random.configure(fg = "green")


root.mainloop()
