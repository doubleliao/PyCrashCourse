current_number = 1
while current_number <= 5:
	print(current_number)
	current_number+= 1

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
	    print(message)

print("\n2")
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)

print("\n3")
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(enter 'quit' when you are finished.)"

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}!")

print("\n4")
