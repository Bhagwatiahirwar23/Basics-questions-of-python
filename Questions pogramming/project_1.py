import random

print('''Welcome to our Game
Enter 1. Paper
Enter 2. Rock
Enter 3. Scissors
''')
lst = ["rock", "scissors", "paper"]
computer = random.choice(lst)
print(computer)
user = input()
# print(computer)
if user == computer:
    print("Draw")

# all the condition of loss
elif computer == "rock" and user == "scissors":
    print("You Loss")

elif computer == "scissors" and user == "paper":
    print("You Loss")

elif computer == 'paper' and user == "rock":
    print("You Loss")

# all the condition of win
elif computer == "rock" and user == "paper":
    print("You Won")

elif computer == "paper" and user == "scissors":
    print("You Won")

elif computer == "scissors" and user == "rock":
    print("You Won")