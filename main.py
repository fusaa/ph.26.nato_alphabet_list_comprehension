
import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas
nato = pandas.read_csv('nato_phonetic_alphabet.csv')
print(nato)
#nato_d = {letter:code for (letter, code) in nato.itertuples(index=False)}
nato_d = {row.letter:row.code for (key, row) in nato.iterrows()}
print(nato_d)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


text = input("Word:")
nato_result = [nato_d[l.upper()] for l in text]
print(nato_result)
