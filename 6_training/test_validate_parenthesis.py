import unittest
import validate_parenthesis as foo

class TestValidateParenthesis(unittest.TestCase):

    def test_first(self):
        string = "())"
        self.assertEqual(foo.minAddToMakeValid(string), 1)
    def test_first(self):
        string = "((("
        self.assertEqual(foo.minAddToMakeValid(string), 3)
    def test_first(self):
        string = "()"
        self.assertEqual(foo.minAddToMakeValid(string), 0)
    def test_first(self):
        string = "()))(("
        self.assertEqual(foo.minAddToMakeValid(string), 4)

if __name__ == "__main__":
    unittest.main()
