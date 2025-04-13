# tests/test_point.py
import unittest
from point import Point

class TestPoint(unittest.TestCase):
    def test_creation(self):
        p = Point(40.7128, -74.0060)
        self.assertEqual(p.latitude, 40.7128)
        self.assertEqual(p.longitude, -74.0060)

if __name__ == "__main__":
    unittest.main()
