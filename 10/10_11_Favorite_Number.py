"""
Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file.
Write a separate program that reads in this value and prints the message, 
“I know your favorite number! It’s _____.”
"""

import json

user_number = input(" what's your favorite number?")

filename = 'user_number.json'
with open(filename, 'w') as f:
	json.dump(user_number, f)

with open(filename) as f:
	user_number = json.load(f)
	print(f"I know your favorite number! It's {user_number}")