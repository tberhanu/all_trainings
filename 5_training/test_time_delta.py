import unittest
import time_delta as foo

class TestTimeDelta(unittest.TestCase):

    def test_first(self):
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0000"

        self.assertEqual(foo.time_delta(t1, t2), 25200)

    def test_second(self):
        t3 = "Sat 02 May 2015 19:54:36 +0530"
        t4 = "Fri 01 May 2015 13:54:36 -0000"

        self.assertEqual(foo.time_delta(t3, t4), 88200)