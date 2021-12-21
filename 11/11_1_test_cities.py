
import unittest
from city_country import formated_city_country

class CityTestCase(unittest.TestCase):

	def test_city_country(self):
		city_country = formated_city_country('shenzhen', 'china')
		self.assertEqual(city_country, 'Shenzhen, China')

	def test_city_country_population(self):
		city_country = formated_city_country('shenzhen', 'china', '5000')
		self.assertEqual(city_country, 'Shenzhen, China, -Population 5000')

if __name__ == '__main__':
	unittest.main()
