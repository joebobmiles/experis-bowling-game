import unittest

from alleygator import ScoreCard

class TestScoreCard(unittest.TestCase):
    def test_can_access_frame_by_index(self):
        """
        You can index a scorecard by frame number.
        """
        for firstFrame in [ [ 0, 8 ], [ 1, 0 ] ]:
            with self.subTest(msg="First frame is {}".format(firstFrame)):
                scoreCard = ScoreCard([
                    firstFrame,
                ])

                self.assertEqual(scoreCard[0], firstFrame)

if __name__ == "__main__":
    unittest.main()