# rock , paper , scissors game

import random

sign =[
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

player_decision = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

print(sign[player_decision])

computer_decision = random.randint(0,2)
print("Computer chose:")
print(sign[computer_decision])

if player_decision == computer_decision:
    print("Draw")
elif player_decision == 0 and computer_decision == 1:
    print("Computer wins")
elif player_decision == 0 and computer_decision == 2:
    print("Player Wins")
elif player_decision == 1 and computer_decision == 0:
    print("Player Wins")
elif player_decision == 1 and computer_decision == 2:
    print("Computer Wins")
elif player_decision == 2 and computer_decision == 0:
    print("Computer Wins")
elif player_decision == 2 and computer_decision == 1:
    print("Player Wins")
else:
    print("Unconsidered rule")
