import requests
from random import choice
import pyfiglet
from termcolor import colored
from colorama import init

init()
ascii_art = pyfiglet.figlet_format("Dad Joke 3000")
print(colored(ascii_art, color="green"))

url = "https://icanhazdadjoke.com/search"
search_term = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params = {"term": search_term}
	)

data = response.json()

results = data["results"]

num_jokes = data["total_jokes"]

joke_amount = ""
if num_jokes > 1:
	print(f"I've got {num_jokes} jokes about {search_term}. Here's one:")
	print(choice(results)["joke"])
elif num_jokes == 1:
	print(f"I've got one joke about {search_term}. Here it is:")
	print(results[0]["joke"])
else:
	print(f"Sorry, I don't have any jokes about {search_term}! Please try again.")

