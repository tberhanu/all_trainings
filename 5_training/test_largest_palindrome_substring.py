import unittest
import largest_palindrome_substring as foo

class TestLargestPalindromeSubstring(unittest.TestCase):

    def test_first(self):
        self.assertEqual(foo.largest_palindrome_substring("hackerrekcahba"), "hackerrekcah")
    def test_two(self):
        self.assertEqual(foo.largest_palindrome_substring("abaddisiddakk"), "addisidda")
    def test_three(self):
        self.assertEqual(foo.largest_palindrome_substring("abcb"), "bcb")