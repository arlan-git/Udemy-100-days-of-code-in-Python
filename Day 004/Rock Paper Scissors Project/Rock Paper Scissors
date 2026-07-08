import random

print("Welcome to the Rock, Paper, Scissors game!")

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

game_images = [rock, paper, scissors]

user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n "))
if user_selection >= 0 and user_selection <= 2:
    print(game_images[user_selection])

cpu_choice = random.randint(0,2)
print("CPU chose:")
print(game_images[cpu_choice])

if user_selection >= 3 or user_selection < 0:
    print("You have typed an invalid number. You lose! Try again!")
elif user_selection == 0 and cpu_choice == 2:
    print("You won!")
elif cpu_choice == 0 and user_selection == 2:
    print("You lost!")
elif cpu_choice > user_selection:
    print("You lose!")
elif user_selection > cpu_choice:
    print("You win!")
elif cpu_choice == user_selection:
    print("Ready for a showdown because its a draw!")
