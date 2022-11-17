import pyfiglet
from termcolor import colored
from colorama import init

init()

colors = ("grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white")

msg = input("What would you like to print? ")
color_input = input("What color? These are the colors you may choose from: (grey, red, green, yellow, blue, magenta, cyan, white)\n")

if color_input not in colors:
	color_input = "green"

ascii_art = pyfiglet.figlet_format(msg)
result = colored(ascii_art, color=color_input)
print(result)