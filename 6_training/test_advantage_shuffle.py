import unittest
import adv_shuffle

class TestAdvCount(unittest.TestCase):

    def test_first(self):
        A = [2, 0, 4, 1, 2]
        B = [1, 3, 0, 0, 2]
        self.assertEqual(adv_shuffle.advantageCount(A, B), [2, 0, 2, 1, 4])
    def test_second(self):
        A = [2,7,11,15]
        B = [1,10,4,11]
        self.assertEqual(adv_shuffle.advantageCount(A, B), [2, 11, 7, 15])
    def test_third(self):
        A = [0]
        B = [0]
        self.assertEqual(adv_shuffle.advantageCount(A, B), [0])
    def test_fourth(self):
        A = [7, 3, 1, 5]
        B = [4, 2, 6, 8]
        self.assertEqual(adv_shuffle.advantageCount(A, B), [5, 3, 7, 1])

if __name__ == "__main__":
    unittest.main()
