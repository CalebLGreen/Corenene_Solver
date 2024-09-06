import pandas as pd
import numpy as np

def initialise():
    with open("four-letter-words.txt", "r") as words:
        four_letter_words = [x.strip() for x in words]
        # print(len(four_letter_words))
        df_a = pd.DataFrame(data=four_letter_words, columns=["Four_Letter_Words"])
    with open("five-letter-words.txt", "r") as words:
        five_letter_words = [x.strip() for x in words]
        # print(len(five_letter_words))
        df_b = pd.DataFrame(data=five_letter_words, columns=["Five_Letter_Words"])
    with open("six-letter-words.txt", "r") as words:
        six_letter_words = [x.strip() for x in words]
        # print(len(six_letter_words))
        df_c = pd.DataFrame(data=six_letter_words, columns=["Six_Letter_Words"])
    # list of data_frames
    dfs = [df_a, df_b, df_c]
    df = pd.concat(dfs,axis=1,keys=["4","5","6"])
    return df


def finder(input_values, all_words):
    correct_searches = {}
    amount_of_chunks = len(input_values)
    for a in range(amount_of_chunks):
        for b in range(amount_of_chunks):
            for c in range(amount_of_chunks):
                word = input_values[a] + input_values[b] + input_values[c]
                correct = try_word(word, all_words)
                if correct:
                    correct_word = {'a': a, 'b' : b, 'c' : c}
                    correct_searches[word] = correct_word

    return correct_searches


def compiler(word_dictionary):
    compiled_words = []
    for word, idx in word_dictionary.items():
        word_idx = []
        for values in idx.values():
            word_idx.append(values)
        compiled_words.append([word, word_idx])
    # print(compiled_words)
    # print(compiled_words)
    correct_words = solver(compiled_words)
    return(correct_words)

def solver(compiled_words):
    amount_of_words = len(compiled_words)
    correct_guesses = []
    for a in range(amount_of_words):
        for b in range(amount_of_words):
            for c in range(amount_of_words):
                if a != b and a != c and b != c: 
                    if compiled_words[a][1][1] == compiled_words[b][1][1] and compiled_words[a][1][1] == compiled_words[c][1][1]:
                        if compiled_words[a][1][0] not in compiled_words[b][1] and compiled_words[a][1][0] not in compiled_words[c][1] and compiled_words[b][1][0] not in compiled_words[c][1]:
                            if compiled_words[a][1][2] not in compiled_words[b][1] and compiled_words[a][1][2] not in compiled_words[c][1] and compiled_words[b][1][2] not in compiled_words[c][1]:
                                if compiled_words[a][1][0] != compiled_words[a][1][2] and compiled_words[b][1][0] != compiled_words[b][1][2] and compiled_words[c][1][0] != compiled_words[c][1][2]:
                                    correct_guesses.append([compiled_words[a][0], compiled_words[b][0], compiled_words[c][0]])
    return correct_guesses
                

def try_word(word : str, df):
    found_word = (df == word).any().any()
    if found_word:
        return True
    else:
        return False


all_words = initialise()

# array = ["h", "es", "nd", "po", "re", "ru", "s"]
array = ["ac", "ds", "f", "i", "n", "nd", "th"]
# array = ["al", "b", "be", "er", "f", "s", "th"]
# array = ["al", "ge", "li", "ne", "ra", "ru", "s"]

found_words = finder(array, all_words)
# print(found_words)
guesses = compiler(found_words)

for i in guesses:
    print(i)
