import unittest
import flatten_nested_arrays as foo

class FlattenNestedArray(unittest.TestCase):

    def test_first(self):
        arr = [1, 2, [3, 4, 5], [6, 7]]
        arr2 = [1, 2, 3, 4, 5, 6, 7]
        flat = list(foo.flatten(arr))
        print("flatfff: {}".format(flat))
        self.assertEqual(flat, arr2)