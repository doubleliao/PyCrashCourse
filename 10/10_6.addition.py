"""
10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a ValueError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
"""


try:
	given_number_a = input("Please give me a number: ")
	given_number_a = int(given_number_a)
	
	given_number_b = input("Please give me another number: ")
	given_number_b = input(given_number_b)
	
except ValueError:
	print("Please enter numbers!")
else:
	result = given_number_a + given_number_b
	print(f"the answer is {result}")