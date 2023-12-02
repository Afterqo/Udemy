import random 
import hangman_art
import hangman_words

game_over = False
word_list = hangman_words.word_list
stages = hangman_art.stages
chosen_word = random.choice(word_list)
length = len(chosen_word)
lives = 6

display = []
for i in range(length):
    display += "_"

print(hangman_art.logo)
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
