import random 
from hangman_art import stages, logo
from hangman_words import word_list

game_over = False
chosen_word = random.choice(word_list)
length = len(chosen_word)
lives = 6

display = []
for i in range(length):
    display += "_"

print(logo)
while not game_over:
    guess = input("Guess a letter: ").lower()

    for i in range(length):
        if guess == chosen_word[i]:
            display[i] = guess
   
    if guess not in chosen_word:
        lives -= 1

    print(stages[lives])
    output = ""
    for char in display:
        output += char + " "
    print(output)

    if lives == 0:
        print("You lost.")
        game_over = True

    if "_" not in display:
        print("You won!")
        game_over = True
