import unittest
from src.rooms import Rooms
from src.guests import Guest
from src.songs import Songs

class TestSongs(unittest.TestCase):

    def setUp(self):
        self.song_1 = Songs("All Night Long")
        self.song_2 = Songs("Dancing Queen")
        self.song_3 = Songs("Barbie Girl")        
        self.song_4 = Songs("Summertime")
        self.song_5 = Songs("Mac The Knife")
        self.song_6 = Songs("Highway To Hell")
        self.song_7 = Songs("Jump")
        self.song_8 = Songs("Dancing Queen")

    def test_song_has_a_title(self):
        self.assertEqual("All Night Long", self.song_1.title)  