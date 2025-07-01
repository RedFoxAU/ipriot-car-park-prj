from sensor import Sensor
from display import Display
from pathlib import Path

class CarPark:
    def __init__(self, location, capacity, plates=None, displays=None, sensors=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."

    def car_entered(self, license_plate):
        print(f"Car entered with plate: {license_plate}")

    def car_exited(self, license_plate):
        print(f"Car exited with plate: {license_plate}")

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        if plate not in self.plates:
            self.plates.append(plate)
            self.update_displays()

    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()
        else:
            raise ValueError(f"Plate {plate} not found in car park.")

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 25}

        for display in self.displays:
            display.update(data)

    @property
    def available_bays(self):
        return max(0, self.capacity - len(self.plates))
