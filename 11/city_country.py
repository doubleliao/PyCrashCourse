"""
Write a function that accepts two parameters: a city name
and a country name. The function should return a single string of the form
City, Country, such as Santiago, Chile. Store the function in a module called
city_functions.py.
"""


def formated_city_country(city, country, population=''):
	if population:
		city_country = (f"{city}, {country}, -population {population}")
	else:
		city_country = f"{city}, {country}"
	return city_country.title()

