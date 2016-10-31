import sys
import random

def read_file():
    with open("/usr/share/dict/words", "r") as f:
        for line in f:
            all_lines = f.read().lower()
            list_words = all_lines.split()
    return list_words

#select word out of list
#Setting easy list (4-6 characters), normal (6 - 8 characters), hard(8 letters or more)
def organize_words(all_words):
    easy_list = []
    normal_list = []
    hard_list = []
    for word in all_words:
        if len(word) >= 4 and len(word) <= 6:
            easy_list.append(word)
        elif len(word) >=6 and len(word) <= 8:
            normal_list.append(word)
        elif len(word) > 8:
            hard_list.append(word)
    return easy_list, normal_list, hard_list

def get_random_word(user_diff_choice, easy, normal, hard):
    random_word = ''
    if user_diff_choice == 'e':
        random_word = random.choice(easy)
    elif user_diff_choice == 'n':
        random_word = random.choice(normal)
    elif user_diff_choice == 'h':
        random_word = random.choice(hard)
    return random_word

def game_welcome():
    print("Hello! Select a difficulty:")
    print("easy (e), normal(n), or hard(h). ")

#let user choose a level of difficulty: easy, normal, or hard.
def difficulty_level():
    diff_select = input("> ").lower()
    accepted_input = ["e", "n", "h"]
    if diff_select not in accepted_input:
        print("you must only enter 'e', 'n', or 'h'")
        main()
    return diff_select

# Write a function to select a word at random from the word list.


#start of game will tell user how many letters the word contains

#ask user to input one letter per round. upper or lowercase doesn't matter.
#if more than one letter is input, tell user input is invalid and try again
#let user know if their guess appears in the computers word.
#display the partially guessed word as well as letter not yet guessed.
#display a word with blanks/letters filled in the appropriate spots.

def draw_word(right_guess, wrong_guess, secret_word):
    duplicate_letters = []
    # print(blanks)
    for letter in secret_word: #replace blanks with correctly guessed letters
        if letter in right_guess:
            print(letter, end=' ')
            duplicate_letters.append(letter)
        else:
            print("_ ", end=' ')

    for letter in secret_word:
        remaining_letters = (len(secret_word) - len(duplicate_letters))
    if remaining_letters == 0:
        win_condition()
        game_reset()

def win_condition():

    print("\nThat's right! You win!")
    game_reset()

def loss_condition(secret_word):

    print("\nYou ran out of guesses!")
    print("The secret word was {}.".format(secret_word))
    game_reset()

def game_reset():
    replay = input("Play again? (Yes(y)/No(n)) ").lower()
    if replay[0] == 'n':
        exit()
    elif replay[0] == 'y':
        main()
    else:
        exit()

# # A user is allowed 8 guesses.
# Remind the user of how many guesses they have left after each round.
# A user loses a guess only when they guess incorrectly.
# If they guess a letter that is in the computer's word, they do not lose a guess.
# If the user guesses the same letter twice, print a message letting them know
# they've already guessed that letter and ask them to try again.
# #The game will end when the user constructs the full word or runs out of guesses.
# If the player runs out of guesses, reveal the word to the user when the game ends.

#When a game ends, ask the user if they want to play again.
#Write a function to check if a word has been completely guessed.

def main():
    right_guess = []
    wrong_guess = []
    all_words = read_file()
    letter_guess = ''
    easy, normal, hard = organize_words(all_words)
    game_welcome()
    user_diff_choice = difficulty_level()
    secret_word = get_random_word(user_diff_choice, easy, normal, hard)
    print(secret_word)
    while len(wrong_guess) <= 8:
        print("\nNumber of guesses remaining {}\n".format(8 - len(wrong_guess)))
        if len(wrong_guess) == 8:
            lose_condition(secret_word)
            game_reset()
        draw_word(right_guess, wrong_guess, secret_word)
        letter_guess = input("\nGuess a letter: ").lower()
        if len(letter_guess) != 1 or not letter_guess.isalpha():
            print("Please guess single letters only")
        elif letter_guess == '':
            print("You have to enter a letter.")
        elif letter_guess in right_guess or letter_guess in wrong_guess:
            print ("\nYou've already guessed that.")
        elif letter_guess in secret_word:
            print("\nGood job that letter is in the word!")
            right_guess.append(letter_guess)
        elif letter_guess not in secret_word:
            print("\nThat letter is not in the word. Try again.")
            wrong_guess.append(letter_guess)



if __name__ == "__main__":
    main()
