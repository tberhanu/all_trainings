import unittest
import max_product_23 as foo

class TestMaxProduct(unittest.TestCase):
    def test_first(self):
        arr = ["abcw","baz","foo","bar","xtfn","abcdef"]

        self.assertEqual(foo.max_product(arr), 16)
    def test_two(self):
        arr = ["a","ab","abc","d","cd","bcd","abcd"]

        self.assertEqual(foo.max_product(arr), 4)
    def test_three(self):
        arr = ["a","aa","aaa","aaaa"]

        self.assertEqual(foo.max_product(arr), 0)


if __name__ == "__main__":
    unittest.main()
