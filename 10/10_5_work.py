"""
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""

filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nwhy do you like programing? ")
    responses.append(response)

    continue_poll = input("would you like to let some else respond? (y/n) ")
    if continue_poll != 'y':
        break
with open(filename, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")
