from coe_number.number_utils import is_prime_list

import unittest
##test
class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
    def test_give_31_37_41_is_prime(self):
        prime_list = [31, 37, 41]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_151_157_163_is_prime(self):
        prime_list = [151, 157, 163]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
    def test_give_421_431_433_is_prime(self):
        prime_list = [421, 431, 433]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_983_991_997_is_prime(self):
        prime_list = [983, 991, 997]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)