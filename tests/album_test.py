import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.album = Album('The Blue Album', 'Rock', 'Weezer')

    def test_album_has_title(self):
        self.assertEqual("The Blue Album", self.album.title)

    def test_album_has_genre(self):
        self.assertEqual("Rock", self.album.genre)

    def test_album_has_artist(self):
        self.assertEqual("Weezer", self.album.artist)