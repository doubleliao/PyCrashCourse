import json

filename = 'user_number.json'
try:
	with open(filename) as f:
		user_number = json.load(f)
except FileNotFoundError:
	user_number = input("what's your favorite number?")
	with open(filename, 'w') as f:
		json.dump(user_number, f)
		print(f"I will remember it. Thanks!")
else:
	print(f"I know your favorite number! It's {user_number}")


