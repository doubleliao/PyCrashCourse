def greet_user():
	"""Display a simple greeting."""
	print("hello!")

greet_user()	

def greet_user(username):
	"""Display a simple greeting."""
	print(f"hello!, {username.title()}!")

greet_user('jesse')

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry')	
describe_pet(animal_type= 'hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type= 'hamster',)

def describe_pet(pet_name, animal_type= 'dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet(pet_name= 'willie')

print("\n2")
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

print("\n3")
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    print(f"{full_name.title()}")

get_formatted_name('jimi', 'hendrix')

print("\n4")
def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

print("\n5")
def build_person(first_name, last_name):
	"""Return a dictionary of information about a person."""
	person = {'first':first_name, 'last': last_name}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=None):
    """Return a dictionary of infotmation about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

print("\n6")
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")

	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}!")



















