#10-3. Guest: Write a program that prompts the user for their name. 
# When theyrespond, write their name to a file called guest.txt.

guest_name = input("please enter your name: ")

filename = 'guest_name.txt'
with open(filename, 'w') as file_object:
	file_object.write(guest_name)

#10-4. Guest Book: Write a while loop that prompts users for their name. When
#they enter their name, print a greeting to the screen and add a line recording
#their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the file.

filename = 'guest_book.txt'

prompt = "\nplease enter your name: "
prompt += "\nEnter 'quit' to end the program. "

while True:
    guest_name = input(prompt)
    if guest_name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{guest_name}\n")
        print(f"Hi, {guest_name}, your name has been recorded in the guest book.")





