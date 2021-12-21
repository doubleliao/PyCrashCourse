alien_0 = {'color': 'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] =5
print(alien_0)

alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

print("\n")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
alien_0['speed'] = 'fast'
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
	# This must be a fast alien.
	x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

print("\n")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

print("\n1")
favorite_language = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
    }

language = favorite_language['sarah'].title()
print(f"sarah's favorite language is {language}.")

print("\n2")
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
    }
for key, value in user_0.items():
	print(f"\nkey: {key}")
	print(f"Value: {value}")

print("\n3")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
    }
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}")
for name in favorite_languages.keys():
	print(name.title())
for name in favorite_languages:
	print(name.title())

print("\n4")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")


print("\n5")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

print("\n6")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

print("\n7")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

print("\n8")
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

# Show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total bumber of aliens: {len(aliens)}")


print("\n9")

# Store information about a pizza being ordered.
pizza = {
	'crust': 'thick',
	'toppings': ['mushroom', 'extra cheese'],
    }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza"
    "with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

print("\n10")
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")

print("\n10")

users = {
	'aeinstein': {
	    'first': 'albert',
	    'last': 'einstein',
	    'location': 'princeton',
	    },
	'murie': {
	    'first': 'marie',
	    'last': 'curie',
	    'location': 'paris',
	    },
    }
for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")


