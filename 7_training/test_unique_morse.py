import unittest
import unique_morse as foo

class TestUniqueMorse(unittest.TestCase):

    def test_first(self):
        words = ["gin", "zen", "gig", "msg"]
        self.assertEqual(foo.uniqueMorseRepresentations(words), 2)


if __name__ == "__main__":
    unittest.main()
