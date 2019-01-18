import unittest
import merge_the_tools as foo

class TestMergeTheTools(unittest.TestCase):

    def test_mytest(self):
        self.assertEqual(foo.merge_the_tools("aabcaaada", 3))