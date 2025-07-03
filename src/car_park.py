import json
from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime

class CarPark:
    def __init__(self, name, capacity, plates=None, sensors=None, displays=None, log_file=Path("log.txt")):
        self.name = name
        self.capacity = capacity
        self.sensors = sensors or []
        self.displays = displays or []
        self.plates = plates or []
        self.log_file = log_file

    def __str__(self):
        return f"Car park at {self.name}, with {self.capacity} bays."

    def car_entered(self, plate):
        self.add_car(plate)
        print(f"Car entered with plate: {plate} \nAvailable bays: {self.available_bays}")

    def car_exited(self, plate):
        self.remove_car(plate)
        print(f"Car exited with plate: {plate} \nAvailable bays: {self.available_bays}")

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
            raise ValueError(f"Plate: {plate} not found in car park.")

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)

    @property
    def available_bays(self):
        return max(0, self.capacity - len(self.plates))
