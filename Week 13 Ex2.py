# Ask the user for a word to search
# Load synonyms from Datamuse API
# https://api.datamuse.com/words?ml=

import requests

search = input("What word to lookup? ")
full_url = "https://api.datamuse.com/words?ml=" + search
print(full_url)

response = requests.get(full_url)

if response:
    print(response.text)

else:
    print("Sorry, could not connect.")
    