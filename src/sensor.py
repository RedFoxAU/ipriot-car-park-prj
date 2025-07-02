from abc import ABC, abstractmethod
import random
class Sensor(ABC):
    def __init__(self, bay_id, sensor_id, occupied, car_park):
        self.bay = bay_id
        self.id = sensor_id
        self.occupied = occupied
        self.car_park = car_park

    @abstractmethod
    def detect_car_entry(self, plate):
        pass

    @abstractmethod
    def detect_car_exit(self, plate):
        pass

    # def detect_car_exit(self):
    #     plate = self._scan_plate()
    #     self.update_car_park(plate)

    def is_occupied(self):
        return self.occupied

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")  # Fake number plate for testing

class EntrySensor(Sensor):
    def detect_car_entry(self, plate):
        if plate is None:
            plate = self._scan_plate()
        self.occupied = True
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    def detect_car_exit(self, plate)
        self.car_park.remove_car(plate)
        self.occupied = False
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

