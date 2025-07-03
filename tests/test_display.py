import unittest
from display import Display
from car_park import CarPark

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display(id=1, message="Welcome to the 1-SPACELEFT-CARPARK", is_on=True)

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the 1-SPACELEFT-CARPARK")
        self.assertTrue(self.display.is_on)

    def test_update(self):
        self.display.update({"message": "VISIT word.audino.net TO PLAY! BYE!"})
        self.assertEqual(self.display.message, "VISIT word.audino.net TO PLAY! BYE!")

if __name__ == "__main__":
    unittest.main()