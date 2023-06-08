import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Dancing Queen", "Abba", "Euro-Pop")

    