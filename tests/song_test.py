import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Dancing Queen", "Abba", "Euro-Pop")

    def test_song_has_name(self):
        self.assertEqual("Dancing Queen", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Abba", self.song.artist)

    def test_song_has_genre(self):
        self.assertEqual("Euro-Pop", self.song.genre)