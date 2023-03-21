import unittest

from alleygator.data import ScoreCard

class TestScoreCard(unittest.TestCase):
    def test_initializes_all_frames_to_zero(self):
        for i in range(0, 8):
            with self.subTest(i=i):
                self.assertEqual(ScoreCard()[i], ( 0, 0 ))

        # The last frame is special!
        with self.subTest(i=9):
            self.assertEqual(ScoreCard()[9], ( 0, 0, 0 ))