import json
from difflib import get_close_matches

dict_data = json.load(open("data.json"))

word = input("Enter the word you would like to translate: \n").lower()

if word.lower() in dict_data.keys():
    count = 0
    for w in dict_data[word.lower()]:
        print("Definition %s: %s" % (count+1, dict_data[word.lower()][count]))
        count += 1
elif word.upper() in dict_data.keys():
    count = 0
    print("Definition %s: %s" % (count + 1, dict_data[word.upper()][count]))
    count += 1
elif get_close_matches(word, dict_data.keys()):
    close_match = get_close_matches(word, dict_data.keys())[0]
    match_word = input("Did you mean '%s' instead?:    Enter Y if yes, and N if no. \n" % close_match).lower()

    if match_word == "y":
        count = 1
        for w in dict_data[close_match]:
            print("Definition %d: %s" % (count, w))
            count += 1
    elif match_word == "n":
        print("Word does not exist! - Please try again with a different word.")
    else:
        print("Word does not exist! - Please try again with a different word.")

else:
    print("Word does not exist! - Please try again with a different word.")
