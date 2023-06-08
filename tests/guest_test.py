import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Greg", 1000)

    def test_guest_has_name(self):
        self.assertEqual("Greg", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(1000, self.guest.wallet)