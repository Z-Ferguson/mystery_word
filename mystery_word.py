#open file
#read file as a whole
#select word out of list
def organize_words():
    with open("/usr/share/dict/words", "r") as f:
        master_word_list = []
        for line in f:
            master_word_list.append(line.strip())
    # print(master_word_list)
    return master_word_list
# print(master_word_list)

#Setting easy list (4-6 characters)
def set_difficulty_list():
    easy_list = []
    medium_list = []
    hard_list = []
    all_words = organize_words()
    # print(all_words)
    for word in all_words:
        if len(word) >= 4 and len(word) <= 6:
            easy_list.append(word)
        elif len(word) >=6 and len(word) <= 8:
            medium_list.append(word)
        elif len(word) > 8:
            hard_list.append(word)
    print(len(easy_list))
    print(len(medium_list))
    print(len(hard_list))

set_difficulty_list()

#let user choose a level of difficulty: easy, normal, or hard.
# def difficulty_level():

    #start of game will tell user how many letters the word contains
def game_start():
    print("hello!")
    print("Enter 'e' for easy, 'n for normal or 'h' for hard")

    #ask user to input one letter per round. upper or lowercase doesn't matter. .upper() or .lower()
    #if more than one letter is input, tell user input is invalid and try again
# def user_input():
#
#
# #let user know if their guess appears in the computers word.
# #display the partially guessed word as well as letter not yet guessed.
# # # Write a function to display a word with blanks/letters filled in the appropriate spots.
# def display_word_guess():
#
# # A user is allowed 8 guesses. # Remind the user of how many guesses they have left after each round.
# # A user loses a guess only when they guess incorrectly.
#     # If they guess a letter that is in the computer's word, they do not lose a guess.
#     #If the user guesses the same letter twice, print a message letting them know they've already guessed that letter and ask them to try again.
# #The game will end when the user constructs the full word or runs out of guesses.
#     # If the player runs out of guesses, reveal the word to the user when the game ends.
# #When a game ends, ask the user if they want to play again.
# def input_analysis():
#
# # Write functions to select a subset of the complete word list.
# def select_subset():
#
#
# # # Write a function to select a word at random from the word list.
# def random_word():
#
#
# # # Write a function to check if a word has been completely guessed.
# def word_check:()
