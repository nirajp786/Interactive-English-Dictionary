import json
from difflib import get_close_matches

def translate(word):
    #word = word.lower()
    if word.lower() in data or word.upper() in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        bestMathch = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys(), cutoff=0.8)[0])
        if (bestMathch.upper() == "Y"):
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif (bestMathch.upper() == "N"):
            return "The word doesn't exist. Please double check it."
        else:
            return "Not a correct option."
        
    else:
        return "The word doesn't exist. Please double check it."

data = json.load(open("data.json"))
word = input("Enter word: ")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
