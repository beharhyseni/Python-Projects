import json
from difflib import get_close_matches

dict_data = json.load(open("data.json"))

word = input("Enter the word you would like to translate: \n")

if word in dict_data.keys():
    print(dict_data[word][0])
elif get_close_matches(word, dict_data.keys()):
    close_match = get_close_matches(word,dict_data.keys())[0]
    match_word = input("Did you mean '%s' instead?:    Enter Y if yes, and N if no. \n" % close_match)

    if match_word == "Y":
       count = 1
       for w in dict_data[close_match]:
           print("Definition %d: %s" % (count, w))
           count+=1
    elif match_word == "N":
        print("Word does not exist! - Please try again with a different word.")
    else:
        print("Word does not exist! - Please try again with a different word.")

else:
    print("Word does not exist! - Please try again with a different word.")