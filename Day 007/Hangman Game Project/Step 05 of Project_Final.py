# Updated the word list to use the 'word_list' from hangman_words.py
# Imported the 'logo' from hangman_art.py and print it at the start of the game
# Imported the hangman 'stages' from hangman_art.py

import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

print(logo)

lives = 6

chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # The code below tells the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You've already guessed {guess}, try again")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # Determines if the letter is not in the chosen_word, print out the letter and let the user know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed the letter {guess}, that's not in the word. You lose a life!")

        if lives == 0:
            game_over = True

            # The print statement below informs the user the correct word they were trying to guess.
            print(f"***********************The word was {chosen_word}! YOU LOSE!**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # The below uses the stages List from the file hangman_art.py for print
    print(stages[lives])
