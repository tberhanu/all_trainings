import unittest
import minion_game as foo

class TestGame(unittest.TestCase):

    def test_first(self):
        self.assertEqual(foo.minion_game("BANANA"), "Stuart 12")

    def test_second(self):
        self.assertEqual(foo.minion_game("BAANANAS"), "Kevin 19")

    def test_third(self):
        self.assertEqual(foo.minion_game("BANANANAAAS"), "Draw")