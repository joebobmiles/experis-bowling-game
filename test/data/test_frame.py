import unittest
import unittest.mock
from alleygator.data import Frame

class TestFrame(unittest.TestCase):
    def test_frame_has_number(self):
        for number in [ 0, 3, 4, 10 ]:
            with self.subTest(msg="Frame # of {}".format(number)):
                self.assertEqual(Frame(number).number, number)

    def test_frame_starts_with_points_of_None(self):
        self.assertEqual(Frame(0).points, [ None, None ])

    def test_frame_starts_with_a_score_of_None(self):
        self.assertEqual(Frame(0).score, None)

    def test_frame_initializes_prev_to_None(self):
        self.assertIsNone(Frame(0).prev)

    def test_frame_initializes_next_to_None(self):
        self.assertIsNone(Frame(0).next)

    def test_can_set_points_on_creation(self):
        self.assertEqual(Frame(0, (4, 0)).points, [ 4, 0 ])

    def test_compute_returns_correct_points_for_open_frame(self):
        cases = [
            {
                "points": (8, 0),
                "result": 8,
            },
            {
                "points": (4, 2),
                "result":6 
            },
        ]

        for case in cases:
            with self.subTest(msg="{} = {}".format(case["points"], case["result"])):
                frame = Frame(0, case["points"])
                self.assertEqual(frame.compute_score(), case["result"])

    def test_compute_returns_correct_points_for_open_frame_with_siblings(self):
        cases = [
            {
                "previous_score": 10,
                "points": (8, 0),
                "result": 18,
            },
            {
                "previous_score": 2,
                "points": (4, 2),
                "result": 8,
            },
        ]

        for case in cases:
            with self.subTest(msg="{} + {} = {}".format(case["previous_score"], case["points"], case["result"])):
                frame1 = Frame(0, case["points"])
                frame1.compute_score = unittest.mock.Mock(return_value=case["previous_score"])

                frame2 = Frame(1, case["points"])
                frame2.prev = frame1
                
                self.assertEqual(frame2.compute_score(), case["result"])

    # Here, orphan strike frames are frames that do not have a 'next' frame.
    def test_compute_returns_correct_points_for_orphan_strike_frames(self):
        cases = [
            {
                "points": (8, "/"),
                "result": None,
            },
            {
                "points": (4, "/"),
                "result": None,
            },
        ]

        for case in cases:
            with self.subTest(msg="{} = {}".format(case["points"], case["result"])):
                frame = Frame(0, case["points"])
                self.assertEqual(frame.compute_score(), case["result"])

    def test_compute_returns_correct_points_for_orphan_strike_frames(self):
        cases = [
            {
                "points": (8, "/"),
                "next_points": 5,
                "result": 15,
            },
            {
                "points": (4, "/"),
                "next_points": 3,
                "result": 13,
            },
        ]

        for case in cases:
            with self.subTest(msg="{} + {} = {}".format(case["points"], case["next_points"], case["result"])):
                frame1 = Frame(0, case["points"])
                frame2 = Frame(0, (case["next_points"], 0))

                frame1.next = frame2

                self.assertEqual(frame1.compute_score(), case["result"])

    def test_set_points_sets_the_point_value_at_specified_index(self):
        frame = Frame(0)

        frame.set_points(0, 1)

        self.assertEqual(frame.points[0], 1)
