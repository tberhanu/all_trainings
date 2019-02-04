import unittest
import matrix_22 as foo

class TestMatrix(unittest.TestCase):
    def test_first(self):
        matrix = [
                  [1,1,1],
                  [1,0,1],
                  [1,1,1]
                ]
        result = [
                  [1,0,1],
                  [0,0,0],
                  [1,0,1]
                ]
        foo.zeroing_rows_and_cols(matrix)
        self.assertEqual(matrix, result)

    def test_second(self):
        matrix = [
                  [0,1,2,0],
                  [3,4,5,2],
                  [1,3,1,5]
                ]
        result = [
                  [0,0,0,0],
                  [0,4,5,0],
                  [0,3,1,0]
                ]
        foo.zeroing_rows_and_cols(matrix)
        self.assertEqual(matrix, result)

if __name__ == "__main__":
    unittest.main()
