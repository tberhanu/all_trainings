import unittest
import reverse_only_letters as foo

class TestReverseONlyLetters(unittest.TestCase):
    def test_first(self):
        self.assertEqual(foo.reverseOnlyLetters("ab-cd#ef"), "fe-dc#ba")
        self.assertEqual(foo.reverseOnlyLetters("a-bC-dEf-ghIj"), "j-Ih-gfE-dCba")
        self.assertEqual(foo.reverseOnlyLetters("Test1ng-Leet=code-Q!"), "Qedo1ct-eeLg=ntse-T!")

if __name__ == "__main__":
    unittest.main()
