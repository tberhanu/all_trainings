import unittest

import qn1fib


class TestQn1fib(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(qn1fib.fib(0), 0)

    def test_fib2(self):
        self.assertEqual(qn1fib.fib(1), 1)

    def test_fib3(self):
        self.assertEqual(qn1fib.fib(2), 1)

    def test_fib4(self):
        self.assertEqual(qn1fib.fib(3), 2)


if __name__ == '__main__':
    unittest.main()