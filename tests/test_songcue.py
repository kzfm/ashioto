import unittest
from ashioto.nameserver import SongCue


class SongCueTest(unittest.TestCase):
    def setUp(self):
        self.cue = SongCue()

    def test_add(self):
        self.assertEqual(1, 2)
