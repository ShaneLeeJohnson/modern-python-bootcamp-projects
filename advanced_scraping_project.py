import requests
from bs4 import BeautifulSoup
import random
from time import sleep

base_url = "http://quotes.toscrape.com"
url = "/page/1"
quotes_list = []

while url:
	response = requests.get(f"{base_url}{url}")
	print(f"Now Scraping {base_url}{url}...")
	soup = BeautifulSoup(response.text, "html.parser")
	quotes = soup.find_all(class_="quote")


	for quote in quotes:
		quote_text = quote.find(class_="text").get_text()
		author = quote.find(class_="author").get_text()
		bio_link = quote.find("a")["href"]
		quotes_list += [[quote_text, author, bio_link]]

	next_btn = soup.find(class_="next")
	url = next_btn.find("a")["href"] if next_btn else None
	sleep(.5)

def quote_game():
	question = quotes_list[random.randint(0, len(quotes_list) - 1)]
	question_text = question[0]
	answer = question[1]
	about_info = question[2]

	response2 = requests.get(f"{base_url}{about_info}")
	soup2 = BeautifulSoup(response2.text, "html.parser")
	date = soup2.find(class_="author-born-date").get_text()
	country = soup2.find(class_="author-born-location").get_text()
	name_list = answer.split(" ")
	hint1 = f"Here's a hint: The author was born: {date} {country}."
	hint2 = f"The author's first initial is {name_list[0][0]}."
	hint3 = f"The author's last initial is {name_list[-1][0]}."

	num_guesses = 4
	while num_guesses > 0:
		print(question_text)
		# print(answer)
		guess = input(f"Can you guess who said this? You have {num_guesses} remaining: ")
		if guess == "quit":
			break

		if guess != answer:
			print("That's incorrect.")
			num_guesses -= 1
			if num_guesses == 3:
				print(hint1)
			elif num_guesses == 2:
				print(hint2)
			elif num_guesses == 1:
				print(hint3)
			else:
				print("You lose!")
				print(f"The author was {answer}.")
		else:
			print("Congratulations you guessed correctly!")
			break
	play_again = input("Would you like to play again? y/n: ")
	if play_again == "y":
		quote_game()

quote_game()