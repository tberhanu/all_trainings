import unittest
import largest_prime_factor as foo

class TestLargestPrimeFactor(unittest.TestCase):

    def test_mytest(self):
        self.assertEqual(foo.largest_prime_factor(17), 17)
    def test_mytest2(self):
        self.assertEqual(foo.largest_prime_factor(13195), 29)

if __name__ == "__main__":
    unittest.main()