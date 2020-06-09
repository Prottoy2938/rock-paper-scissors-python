import random

print("\n...Rock...\n...Paper...\n...Scissors...\n")

print("===========Your Move===============")

# userInput input
userInput = input("What's your move? Answer: ").lower()

# Checking for valid input
while userInput != 'rock' and userInput != 'paper' and userInput != 'scissors':
    print(f"\n \"{userInput}\" is not a valid move")
    print("!!!.....Write a valid move (Rock, Paper or Scissors)...!!!\n")
    userInput = input("What's valid your move? Answer: ").lower()


randNum = random.randint(1, 3)
# picking move based on random number
if randNum == 1:
    computerInput = 'rock'
elif randNum == 2:
    computerInput = 'paper'
elif randNum == 3:
    computerInput = 'scissors'

print(f"\n\nComputer plays: {computerInput}")

print('\n \n=============================================')


# Game Logic
if userInput == computerInput:
    print("Nobody wins!. Its a draw. Try Again")
elif userInput == "rock" and computerInput == "scissors":
    print("You Win!")
elif userInput == "paper" and computerInput == "rock":
    print("You Win!")
elif userInput == "scissors" and computerInput == "paper":
    print("You Win!!!")
else:
    print("Computer Wins!!!")

print('=============================================')
