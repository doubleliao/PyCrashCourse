"""
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.
"""

while True:
	given_number_a = input("Please give me a number: , you can enter'q' to finish.")
	if given_number_a == 'q':
		break
	
	given_number_b = input("Please give me another number: ")

	try:
		result = int(given_number_a) + int(given_number_b)
	except ValueError:
		print("Please enter numbers!")
	else:
		print(f"the answer is {result}")
		
	