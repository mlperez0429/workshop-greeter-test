import unittest

from greeter import greet


class GreetTests(unittest.TestCase):
    def test_greets_a_named_person(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_uses_a_friendly_fallback_for_blank_input(self):
        self.assertEqual(greet("   "), "Hello, friend!")


if __name__ == "__main__":
    unittest.main()
