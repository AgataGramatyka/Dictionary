import json
import string
from difflib import SequenceMatcher, get_close_matches

data = json.load(open('data.json'))

def lookup(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean {} instead? Enter Y for Yes or N for No \n".format(get_close_matches(word, data.keys())[0]))
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return "The word doesn't exist. Please double check"
        else:
            return "Sorry, I didn't understand your query"

    else:
        return "The word doesn't exist. Please double check"

key = input('Please enter a word \n')
output = lookup(key)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
