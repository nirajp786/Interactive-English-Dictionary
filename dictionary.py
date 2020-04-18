import json

def translate(word):
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist. Please double check it."

data = json.load(open("data.json"))
word = input("Enter word: ")

print(translate(word))