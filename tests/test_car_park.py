import unittest
from src.car_park import CarPark

class TestCarPark(unittest.TestCase):
    def test_init(self):
        cp = CarPark(location="Test Lot", capacity=10)
        self.assertEqual(cp.location, "Test Lot")
        self.assertEqual(cp.capacity, 10)
        self.assertEqual(cp.plates, [])
        self.assertEqual(cp.displays, [])

if __name__ == "__main__":
    unittest.main()
