print("...Rock...\n...Paper...\n...Scissors...\n")

print("===========Player1===============")

# player1 input
player1 = input("What's your move? Answer: ").lower()

# Checking for valid input
while player1 != 'rock' and player1 != 'paper' and player1 != 'scissors':
    print(f"\n \"{player1}\" is not a valid move")
    print("!!!.....Write a valid move (Rock, Paper or Scissors)...!!!\n")
    player1 = input("Player1, What's valid your move? Answer: ").lower()

# Using loop to hide the `player1` input
print("!!!!============================= NO CHEATING =============================!!!!\n" * 60)


print("\n===========Player2===============")

# player2 input
player2 = input("What's your move? Answer: ").lower()

# Checking for valid input
while player2 != 'rock' and player2 != 'paper' and player2 != 'scissors':
    print(f"\n \"{player2}\" is not a valid move")
    print("!!!.....Write a valid move (Rock, Paper or Scissors)...!!!\n")
    player2 = input("Player2, What's your valid move? Answer: ").lower()


print('\n \n=============================================')


# Game Logic
if player1 == player2:
    print("Nobody wins!. Its a draw. Try Again")
elif player1 == "rock" and player2 == "scissors":
    print("player1 wins!!!")
elif player1 == "paper" and player2 == "rock":
    print("player1 wins!!!")
elif player1 == "scissors" and player2 == "paper":
    print("player1 wins!!!")
else:
    print("player2 wins!!!")

print('=============================================')
