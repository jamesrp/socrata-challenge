import rotate
import unittest

class TestRotateFunctions(unittest.TestCase):

    def test_degrees_traveled(self):
        # Two tests from the problem description
        self.assertEqual(rotate.degrees_traveled("10:15 AM","12:45 PM"), 900)
        self.assertEqual(rotate.degrees_traveled("10:00 PM","9:00 PM"), 8280)

    def test_timestring_to_minutes(self):
        # Should do the right thing on regular times
        self.assertEqual(rotate.timestring_to_minutes("9:45 AM"), 585)
        self.assertEqual(rotate.timestring_to_minutes("11:45 PM"), 1425)

        # Should handle 12:xx AM and 12:xx PM correctly
        self.assertEqual(rotate.timestring_to_minutes("12:00 PM"), 720)
        self.assertEqual(rotate.timestring_to_minutes("12:15 AM"), 15)
        
        # Should raise error on non-spec input
        with self.assertRaises(ValueError):
            rotate.timestring_to_minutes("19:45 AM")
        with self.assertRaises(ValueError):
            rotate.timestring_to_minutes("9:60 PM")
        with self.assertRaises(ValueError):
            rotate.timestring_to_minutes("from evil_module import *")


if __name__ == '__main__':
    unittest.main()
