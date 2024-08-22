import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phoentic_dict = {row.letter:row.code for(index,row) in data.iterrows()}
# print(phoentic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def pheonitic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phoentic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabets please.")
        pheonitic()
    else:
        print(output_list)

pheonitic()