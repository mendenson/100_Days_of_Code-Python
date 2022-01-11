import random

print("\n")
print("#############################\nRock, Paper, Scissors Game\n#############################\n")

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
# list of choices
game = [rock, paper, scissors]

# user choice 
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Sciccors.\n")

# print user choice
print(game[int(user_choice)])

# computer randomisation
computer_choice = random.randint(0, 2)

#print computer choice
print(f"Computer chose {game[int(computer_choice)]}.\n")

# programming game possibilities
if user_choice == "0":
    if computer_choice == 0:
        print("Draw!\n")
    elif computer_choice == 1:
        print("You lose!\n")
    else:
        print("You win!\n")
elif user_choice == "1":
    if computer_choice == 0:
        print("You win!\n")
    elif computer_choice == 1:
        print("Draw!\n")
    else:
        print("You lose!\n")
else:
    if computer_choice == 0:
        print("You lose!\n")
    elif computer_choice == 1:
        print("You win!\n")
    else:
        print("Draw!\n")
