print("Welcome to Rock, Paper, Scissors!")
player_1_choice = input("Enter player 1's choice: ")
print("***NO CHEATING!!!\n" * 50)
player_2_choice = input("Enter player 2's choice: ")

# if player_1_choice == player_2_choice:
# 	print("Draw!")
# elif player_1_choice == "rock" and player_2_choice == "scissors":
# 	print("Player 1 wins!")
# elif player_1_choice == "rock" and player_2_choice == "paper":
# 	print("Player 2 wins!")
# elif player_1_choice == "scissors" and player_2_choice == "paper":
# 	print("Player 1 wins!")
# elif player_1_choice == "scissors" and player_2_choice == "rock":
# 	print("Player 2 wins!")
# elif player_1_choice == "paper" and player_2_choice == "rock":
# 	print("Player 1 wins!")
# elif player_1_choice == "paper" and player_2_choice == "scissors":
# 	print("Player 2 wins!")
# else:
# 	print("Something went wrong")


# logic refactored #
if player_1_choice == player_2_choice:
	print("Draw!")
elif player_1_choice == "rock":
	if player_2_choice == "scissors":
		print("Player 1 wins!")
	elif player_2_choice == "paper":
		print("Player 2 wins!")
elif player_1_choice == "scissors":
	if player_2_choice == "paper":
		print("Player 1 wins!")
	elif player_2_choice == "rock":
		print("Player 2 wins!")
elif player_1_choice == "paper":
	if player_2_choice == "rock":
		print("Player 1 wins!")
	elif player_2_choice == "scissors":
		print("Player 2 wins!")
else:
	print("Something went wrong")