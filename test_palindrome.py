import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):

    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("arara"))

    def test_phrase_palindrome(self):
        self.assertTrue(is_palindrome("A sacada da casa"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("python"))

    def test_with_numbers(self):
        self.assertTrue(is_palindrome("12321"))
        self.assertFalse(is_palindrome("12345"))

    def test_mixed_case(self):
        self.assertTrue(is_palindrome("Radar"))


if __name__ == "__main__":
    unittest.main()
