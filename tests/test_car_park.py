import unittest
from car_park import CarPark
from pathlib import Path

class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.log_path = Path("log.txt")
        self.car_park = CarPark("123 Example Street", 100, log_file=self.log_path)

    def tearDown(self):
        self.log_path.unlink(missing_ok=True)

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
      #  self.assertEqual(self.car_park.log_file, Path("log.txt"))
        self.assertEqual(self.car_park.log_file, self.log_path)

    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

    def test_register_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.car_park.register("Not a Sensor or Display")

    def test_log_file_created(self):
        new_carpark = CarPark("123 Example Street", 100, log_file = "new_log.txt")
        self.assertTrue(Path("new_log.txt").exists())

    def test_car_logged_when_entering(self):
        self.car_park.add_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)
        self.assertIn("entered", last_line)
        self.assertIn("\n", last_line)

    def test_car_logged_when_exiting(self):
        new_carpark = CarPark("123 Example Street", 100, log_file = "new_log.txt") # TODO: change this to use a class attribute or new instance variable
        self.car_park.add_car("NEW-001")
        self.car_park.remove_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        # self.assertIn(last_line, "NEW-001")
        # self.assertIn(last_line, "exited")
        # self.assertIn(last_line, "\n")
        self.assertIn("NEW-001", last_line)
        self.assertIn("exited", last_line)
        self.assertIn("\n", last_line)

    def test_write_and_load_config(self):
        self.car_park.write_config("test_config.json")
        loaded = CarPark.from_config("test_config.json")
        self.assertEqual(loaded.location, self.car_park.location)
        self.assertEqual(loaded.capacity, self.car_park.capacity)
        self.assertEqual(str(loaded.log_file), str(self.car_park.log_file))
        Path("test_config.json").unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
