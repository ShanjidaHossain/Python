# Shanjida Hossain -- 2/14/2022 --
# Random, List, If else elif

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Write your code below this line 👇
game_image = [rock, paper, scissors]

print("Lets Play Rock-Paper-Scissor")
user_choice = int(input("What do you choose: \n0 - Rock \n1 - Paper \n2 - Scissor\nEnter Here: "))

if user_choice >= 3 or user_choice < 0:
    print("You type invalid number! ")
else:
    print(game_image[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer choose:")
    print(game_image[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win ! ")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose ! ")
    elif user_choice > computer_choice:
        print("You Win! ")
    elif computer_choice > user_choice:
        print("You lose")
    elif computer_choice == user_choice:
        print("It's a Draw !")
