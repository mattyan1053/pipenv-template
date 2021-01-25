from unittest import TestCase
from lib import mylib


class TestMyLib(TestCase):


    def test_mylib(self):
        self.assertEqual(mylib.mylib(), "This is My Test Library!")
