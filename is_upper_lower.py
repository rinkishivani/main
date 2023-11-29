import unittest

import unittest
from upper_lower import is_prime


class TestPrime(unittest.TestCase):
    def setUp(self):
        print("\nRunning setUp method...")

    def tearDown(self):
        print("Running tearDown method...")
    def test_prime_not_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(11))

    def test_typeerror_1(self):
        with self.assertRaises(TypeError):
            # breakpoint()
            is_prime(6.5)

    def test_typeerror_2(self):
        with self.assertRaises(TypeError):
            is_prime('five')

    def test_valueerror(self):
        with self.assertRaises(ValueError):
            is_prime(-4)


# from upper_lower import upper_lower
# class TestUpperLower(unittest.TestCase):
#     def raise_exception_upper_to_lower(self):
#         self.assertRaises(TypeError, upper_lower,)
#     def test_upper_to_lower_vice_versa(self):
#         self.assertEqual(upper_lower('rINKI', 'Rinki'))
#         # self.assertEqual('asd', 'ASD')
#         # self.assertEqual('HELLOO', 'helloo') # add assertion here


if __name__ == '__main__':
    unittest.main()
