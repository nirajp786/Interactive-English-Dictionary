import json
from difflib import get_close_matches

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        return "Did you mean %s instead?" % get_close_matches(word, data.keys(), cutoff=0.8)[0]
        
    else:
        return "The word doesn't exist. Please double check it."

data = json.load(open("data.json"))
word = input("Enter word: ")

print(translate(word))
