#0
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
#1
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
#2
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇
import random

print("RPS simulator\n")
wanna_play = True

while wanna_play:
    player = input("What do you choose ? 'Rock', 'Paper', 'Scissors' ?\n").lower()

    if player != "rock" and player != "paper" and player != "scissors":
        print("Invalid choice\n")
        continue
    else:
        if player == "rock":
            print(rock)
        elif player == "paper":
            print(paper)
        else:
            print(scissors)
        
        computer_choice = random.randint(0, 2)
        if computer_choice == 0:
            computer = "rock"
            print(rock)
        elif computer_choice == 1:
            computer = "paper"
            print(paper)
        else:
            computer = "scissors"
            print(scissors)

        if player == computer:
            print("It's a draw !\n")
        elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
            print("You win !!!\n")
        else:
            print("You lost.\n")
        
        another = input("Do you want to go another round ? 'Y', 'N' ?\n").lower()
        if another == "n":
            wanna_play = False