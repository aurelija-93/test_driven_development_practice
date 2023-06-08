import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Disco Beats")
        self.guest = Guest("Greg", 1000)
        self.song = Song("Dancing Queen", "Abba", "Euro-Pop")

    def test_room_has_name(self):
        self.assertEqual("Disco Beats", self.room.name)

    def test_room_has_empty_song_list(self):
        self.assertEqual(0, len(self.room.song_list))

    def test_can_add_song(self):
        self.room.add_song(self.song)
        self.assertEqual(1, len(self.room.song_list))

    def test_room_has_empty_guest_list(self):
        self.assertEqual(0, len(self.room.guest_list))

    def test_can_add_guest(self):
        self.room.add_guest(self.guest)
        self.assertEqual(1, len(self.room.guest_list))

    def test_can_remove_guest(self):
        self.room.add_guest(self.guest)
        self.room.remove_guest(self.guest)
        self.assertEqual(0, len(self.room.guest_list))