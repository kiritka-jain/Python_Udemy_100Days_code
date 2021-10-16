import pandas

nato_states = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_series = {rows.letter:rows.code for (index,rows) in nato_states.iterrows()}


entered_word = input("PLease enter a word:").upper()
result =[alphabet_series[letter] for letter in entered_word]
print(result)
