import unittest
import largest_palindrome as foo

class TestLargestPalindrome(unittest.TestCase):

    def test_first(self):
        self.assertEqual(foo.largest_palindrome(1000000), 906609)

if __name__ == "__main__":
    unittest.main()