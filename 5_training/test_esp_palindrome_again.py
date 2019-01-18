import unittest
import esp_palindrome_again as foo


class TestEspPalindromeAgain(unittest.TestCase):
    def test_substrCount(self):
        self.assertEqual(foo.substrCount(5, "asasd"), 7)
        self.assertEqual(foo.substrCount(4, "aaaa"), 10)


if __name__ == "__main__":
    unittest.main()