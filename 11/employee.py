""" 
Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes.
Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.

Write a test case for Employee. Write two test methods, test_give_default
_raise() and test_give_custom_raise(). Use the setUp() method so you don’t
have to create a new employee instance in each test method. Run your test
case, and make sure both tests pass.
"""

class Employee:
    
    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name.title()
        self.l_name = l_name.title()
        self.salary = salary  
        
    def give_raise(self, raise_salary=5000):
        self.salary += raise_salary

