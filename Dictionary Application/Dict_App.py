import json


dict_data = json.load(open("data.json"))

word = input("Enter the word you would like to translate: ")

if word in dict_data.keys():
    print(dict_data[word][0])
else:
    print("Word does not exist. Please try again with a different word.")