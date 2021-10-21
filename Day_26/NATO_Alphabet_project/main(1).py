import pandas

nato_states = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_series = {rows.letter:rows.code for (index,rows) in nato_states.iterrows()}

def generate_phonetic():
    entered_word = input("PLease enter a word:").upper()
    try:
        result =[alphabet_series[letter] for letter in entered_word]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()