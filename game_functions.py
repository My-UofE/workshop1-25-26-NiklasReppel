import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = poss_values[(len(poss_values)//2)]
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if(user_input == 'h'):
        if(current_val < next_val):
            return True
        return False
    elif(user_input == 'l'):
        if(current_val > next_val):
            return True
        return False
    return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    indicies = all_indicies(word, letter)
    for i in indicies:
        board[i] = letter
    if len(list(indicies)) > 0:
        print("Well done! '" + letter + "' can be found in the word.")
        return True
    print("Sorry! '" + letter + "' can not be found in the word.")
    return False

def all_indicies(word, letter):
    word_list = list(word)
    index_list = []
    for i in range(len(word_list)):
        if word_list[i] == letter:
            index_list.append(i)
    return index_list