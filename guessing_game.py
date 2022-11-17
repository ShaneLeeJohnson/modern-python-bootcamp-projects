import random

# basic version
# random_number = random.randint(1,10)

# guess = None

# while guess != random_number:
# 	guess = int(input("Guess a number from 1 to 10: "))
# 	if guess < random_number:
# 		print("Too low!")
# 	elif guess > random_number:
# 		print("Too high!")
# 	else:
# 		print("You win!")

# advanced version
random_number = random.randint(1,10)

while True:
	guess = int(input("Guess a number from 1 to 10: "))
	if guess < random_number:
		print("Too low!")
	elif guess > random_number:
		print("Too high!")
	else:
		print("You win!")
		play_again = input("Do you want to play again? (y/n) ")
		if play_again == "y":
			random_number = random.randint(1,10)
			guess = None
		else:
			print("Thank you for playing!")
			break