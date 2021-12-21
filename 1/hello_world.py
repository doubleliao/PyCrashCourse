print("hello python world!")
message= "hello liaoliao!"
print(message)

message = "hello python crash course world"
print(message)
print(message)

name = "ada lovelace"
print(name.title())

name = "aDA llovelace"
print(name.upper())
print(name.lower())

x, y, z = 0, 1, 2
print(z)

motorcycles = ['honda', 'yamha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('apple')
print(motorcycles)
motorcycles.insert(0, 'apple')
print(motorcycles)

print("\n")
motorcycles = ['honda', 'yamha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print("\n")
motorcycles = ['honda', 'yamha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")

print("\n")
motorcycles = ['honda', 'yamha', 'suzuki', 'ducati']

print("\n")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
	print(f"{magician.title()}, that was a great trick")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")


for value in range(1, 5):
	print(value)

numbers = list(range(1, 6))
print(numbers)

print("\n")
even_numbers = list(range(2, 11, 2))
print(even_numbers)
even_numbers = list(range(2, 11, ))
print(even_numbers)

print("\n")
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)

print("\n")
suares = [value**2 for value in range(1,11)]
print(squares)

print("\n")

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[-4:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

print("\n")
new_players = players[:]
print(new_players)
players.append('AA')
new_players.append('BB')
print(players)
print(new_players)

my_t = (3, 2)
print(my_t)
print(my_t[0])


my_ts = (3)

print(my_ts)

print("\n")

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchoviess")

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")


age = 19
if age >= 18:
    print("you are old enough to vote!")
    print("Please register to vote as soon as you turn 18!")
else:
    print("sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


print("\n")
requested_topping = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topping:
	print("adding mushrooms")
if 'pepperoni' in requested_topping:
	print("adding pepperoni")
if 'extra cheese' in requested_topping:
	print("adding extra cheese.")
print("\nfinished making your pizza")


print("\n")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
	    print("sorry, we are out of green peppers right now.")
	else:
		print(f"adding {requested_topping}.")
print("\nfinished making your pizza!")

print("\n1")
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"adding  {requested_topping}.")
	print("\nfinished making your pizza!")
else:
	print("are you sure you want a plain pizza?")

print("\n2")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"adding {requested_topping}.")
	else:
		print(f"sorry, we don't have {requested_topping}.")
print("\nfinished making your pizza!")










