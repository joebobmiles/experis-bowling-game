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

    def test_set_points_sets_the_point_value_at_specified_index(self):
        frame = Frame(0)

        frame.set_points(0, 1)

        self.assertEqual(frame.points[0], 1)

    def test_subscribers_are_alerted_to_points_changes(self):
        frame = Frame(0)

        for i in [ 0, 1 ]:
            with self.subTest(i=i):
                callback = unittest.mock.Mock()
                frame.subscribe_to_points(i, callback)

                frame.set_points(i, 1)

                callback.assert_called_once()

    def test_subscriber_callbacks_are_provided_new_point_value(self):
        frame = Frame(0)

        for i in [ 0, 1 ]:
            with self.subTest(i=i):
                callback = unittest.mock.Mock()
                frame.subscribe_to_points(i, callback)

                frame.set_points(i, 2)

                callback.assert_called_with(2)