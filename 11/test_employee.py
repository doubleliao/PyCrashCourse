"""
Write a test case for Employee. Write two test methods, test_give_default
_raise() and test_give_custom_raise(). Use the setUp() method so you don’t
have to create a new employee instance in each test method. Run your test
case, and make sure both tests pass.
"""
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.a_employee = Employee('double', 'liao', 1000)
    
    def test_give_default_raise(self):
        self.a_employee.give_raise()
        self.assertEqual(self.a_employee.salary, 6000)
        
    def test_give_custom_raise(self):
        self.a_employee.give_raise(2000)
        self.assertEqual(self.a_employee.salary, 3000)
        
if __name__ == '__main__':
    unittest.main()