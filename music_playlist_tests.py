import unittest
from music_playslist_6 import Playlist

class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.playlist = Playlist()
        self.playlist.add_song("A", "Artist1")
        self.playlist.add_song("B", "Artist2")
        self.playlist.add_song("C", "Artist3")

    def test_current_song(self):
        self.assertEqual(self.playlist.current_song().title, "A")

    def test_next_previous_song(self):
        self.playlist.next_song()
        self.assertEqual(self.playlist.current_song().title, "B")
        self.playlist.previous_song()
        self.assertEqual(self.playlist.current_song().title, "A")

    def test_remove_song(self):
        self.assertTrue(self.playlist.remove_song("B"))
        self.playlist.next_song()
        self.assertEqual(self.playlist.current_song().title, "C")
        self.assertFalse(self.playlist.remove_song("X"))