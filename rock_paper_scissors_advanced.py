import random

player_wins = 0
computer_wins = 0
winning_score = 3

print("Let's Play Rock, Paper, Scissors!")

while player_wins < winning_score and computer_wins < winning_score:
	print(f"Player Score: {player_wins} Computer Score: {computer_wins}")

	choices = ["rock", "paper", "scissors"]

	rand_num = random.randint(0,2)
	player_choice = input("Enter your choice: ").lower()
	if player_choice == "quit" or player_choice == "q":
		break
	computer_choice = choices[rand_num]

	if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
		if player_choice == computer_choice:
			print(f"computer chose {computer_choice}")
			print("Draw!")
		elif player_choice == "rock" and computer_choice == "scissors":
			print(f"computer chose {computer_choice}")
			print("You win!")
			player_wins += 1
		elif player_choice == "paper" and computer_choice == "rock":
			print(f"computer chose {computer_choice}")
			print("You win!")
			player_wins += 1
		elif player_choice == "scissors" and computer_choice == "paper":
			print(f"computer chose {computer_choice}")
			print("You win!")
			player_wins += 1
		else:
			print(f"computer chose {computer_choice}")
			print("Computer wins!")
			computer_wins += 1
	else:
		print("something went wrong")
if player_wins > computer_wins:
	print("Congrats! You won!")
elif player_wins == computer_wins:
	print("It's a tie")
else:
	print("Oh No! The computer won :(")
print(f"FINAL SCORES... Player Score: {player_wins} Computer Score: {computer_wins}")