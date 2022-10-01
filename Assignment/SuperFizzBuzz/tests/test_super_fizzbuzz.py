import unittest
from SuperFizzBuzz.src.super_fizzbuzz import super_fizzbuzz

class SuperFizzBuzzMod3(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        num = 3
        test = super_fizzbuzz(num)
        self.assertEqual('Fizz', test, 'Fizz')
    
    def test_give_middle_bordery(self):
        num = 5001
        test = super_fizzbuzz(num)
        self.assertEqual('Fizz', test, 'Fizz')
                         
    def test_give_highest_bordery(self):
        num = 9996
        test = super_fizzbuzz(num)
        self.assertEqual('Fizz', test, 'Fizz')
        
class SuperFizzBuzzMod5(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        num = 5
        test = super_fizzbuzz(num)
        self.assertEqual('Buzz', test, 'Buzz')
        
    def test_give_middle_bordery(self):
        num = 5005
        test = super_fizzbuzz(num)
        self.assertEqual('Buzz', test, 'Buzz')
        
    def test_give_highest_bordery(self):
        num = 9995
        test = super_fizzbuzz(num)
        self.assertEqual('Buzz', test, 'Buzz')
        
class SuperFizzBuzzMod9(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        num = 9
        test = super_fizzbuzz(num)
        self.assertEqual('FizzFizz', test, 'FizzFizz')

    def test_give_middle_bordery(self):
        num = 4986
        test = super_fizzbuzz(num)
        self.assertEqual('FizzFizz', test, 'FizzFizz')

    def test_give_highest_bordery(self):
        num = 9999
        test = super_fizzbuzz(num)
        self.assertEqual('FizzFizz', test, 'FizzFizz')
        
class SuperFizzBuzzMOd25(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        num = 25
        test = super_fizzbuzz(num)
        self.assertEqual('BuzzBuzz', test, 'BuzzBuzz')

    def test_give_middle_bordery(self):
        num = 5000
        test = super_fizzbuzz(num)
        self.assertEqual('BuzzBuzz', test, 'BuzzBuzz')

    def test_give_highest_bordery(self):
        num = 10000
        test = super_fizzbuzz(num)
        self.assertEqual('BuzzBuzz', test, 'BuzzBuzz')
        
class SuperFizzBuzzMod3and5(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        num = 15
        test = super_fizzbuzz(num)
        self.assertEqual('FizzBuzz', test, 'FizzBuzz')

    def test_give_middle_bordery(self):
        num = 5010
        test = super_fizzbuzz(num)
        self.assertEqual('FizzBuzz', test, 'FizzBuzz')

    def test_give_highest_bordery(self):
        num = 9975
        test = super_fizzbuzz(num)
        self.assertEqual('FizzBuzz', test, 'FizzBuzz')
        
class SuperFizzBuzzMod9and25(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        num = 225
        test = super_fizzbuzz(num)
        self.assertEqual('FizzFizzBuzzBuzz', test, 'FizzFizzBuzzBuzz')

    def test_give_middle_bordery(self):    
        num = 5175
        test = super_fizzbuzz(num)
        self.assertEqual('FizzFizzBuzzBuzz', test, 'FizzFizzBuzzBuzz')
        
    def test_give_highhest_bordery(self):
        num = 9900
        test = super_fizzbuzz(num)
        self.assertEqual('FizzFizzBuzzBuzz', test, 'FizzFizzBuzzBuzz')

class SuperFizzBuzzNotmacthcase(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        num = 1
        test = super_fizzbuzz(num)
        self.assertEqual('NoFizzBuzz', test, 'NoFizzBuzz')
        
    def test_give_middle_bordery(self):
        num = 5002
        test = super_fizzbuzz(num)
        self.assertEqual('NoFizzBuzz', test, 'NoFizzBuzz')
        
    def test_give_highhest_bordery(self):
        num = 9998
        test = super_fizzbuzz(num)
        self.assertEqual('NoFizzBuzz', test, 'NoFizzBuzz')