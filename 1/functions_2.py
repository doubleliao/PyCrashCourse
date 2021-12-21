def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
		msg = f"Hello, {name.title()}!"
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


print("\n1")
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"printing model: {current_design}")
	completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)


print("\n2")
def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design, until none are left.
	Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed."""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)


print("\n3")
def make_pizza(*toppings):
	"""Print the list of toppings that have been requested."""
	print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')


print("\n4")
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein',
	                        location='princeton',
	                        field='physics')
print(user_profile)


























