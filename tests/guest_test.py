import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Greg", 1000, "Dancing Queen")

    def test_guest_has_name(self):
        self.assertEqual("Greg", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(1000, self.guest.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Dancing Queen", self.guest.favourite_song)

    def test_guest_has_cash__True(self):
        result = self.guest.has_cash(10)
        self.assertTrue(result)

    def test_guest_has_cash__False(self):
        result = self.guest.has_cash(5000)
        self.assertFalse(result)

    def test_remove_cash__successful(self):
        self.guest.remove_cash(10)
        self.assertEqual(990, self.guest.wallet)

    def test_remove_cash__unsuccessful(self):
        self.guest.remove_cash(10000)
        self.assertEqual(1000, self.guest.wallet)

    def test_guest_can_whoo(self):
        result = self.guest.whoo()
        self.assertEqual("Whoo!", result)

    def test_guest_can_boo(self):
        result = self.guest.boo()
        self.assertEqual("Boo!", result)