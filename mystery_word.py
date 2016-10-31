import random

def organize_words():
    with open("/usr/share/dict/words", "r") as f:
        master_word_list = []
        for line in f:
            master_word_list.append(line.strip())
    return master_word_list

#select word out of list
#Setting easy list (4-6 characters), normal (6 - 8 characters), hard(8 letters or more)
def set_difficulty_list(master_word_list):
    easy_list = []
    normal_list = []
    hard_list = []
    diff_list = [easy_list, normal_list, hard_list]
    # all_words = organize_words()
    for word in master_word_list:
        if len(word) >= 4 and len(word) <= 6:
            easy_list.append(word)
        elif len(word) >=6 and len(word) <= 8:
            normal_list.append(word)
        elif len(word) > 8:
            hard_list.append(word)
    return diff_list

#let user choose a level of difficulty: easy, normal, or hard.
def difficulty_level():
    # total_list = set_difficulty_list()
    while True:
        user_select = input("Select a difficulty, easy, normal, or hard ").lower()
        if user_select == "easy":
            return total_list[0]
        # print(len(total_list[0]))
        elif user_select == "normal":
            return total_list[1]
        # print(len(total_list[1]))
        else:
            user_select == "hard"
            return total_list[2]

# Write a function to select a word at random from the word list.
def random_word():
    word_list = difficulty_level()
    # print(random.choice(word_list))
    return random.choice(word_list)

#start of game will tell user how many letters the word contains
def secret_word(word_list):
    # the_secret_word = random_word()
    print(word_list)
    print("Your word has {} letters! ".format(len(the_secret_word)))
    return secretWord

#ask user to input one letter per round. upper or lowercase doesn't matter.
#if more than one letter is input, tell user input is invalid and try again
#let user know if their guess appears in the computers word.
#display the partially guessed word as well as letter not yet guessed.
#display a word with blanks/letters filled in the appropriate spots.

def word_draw(secretWord):

    # secretWord = secret_word()
    letter = " "
    duplicate_letters = []
    guess_input = input("Enter a letter for a guess! ").lower()

    if letter in secretWord:
        right_guess.append(letter)
        return letter
    else:
        letter not in secretWord
        wrong_guess.append(letter)
        return letter

    # print(blanks)
    for letter in secretWord: #replace blanks with correctly guessed letters
        if guess_input in right_guess:
            print(guess_input, end=' ')
            duplicate_letters.append(guess_input)
        else:
            print("_ ", end=' ')

    # for letter in secret_word:
    #        letters_remaining = (len(secret_word) - len(duplicate_letters))


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

    master_word_list = organize_words()
    diff_list = set_difficulty_list(master_word_list)
    word_list = difficulty_level(master_word_list, diff_list)
    total_list = random_word()
    secretWord = secret_word(word_list)

random_word()



main()
