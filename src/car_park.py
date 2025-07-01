from sensor import Sensor
from display import Display
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

    def register(self, obj):
        if isinstance(obj, Display):
            self.displays.append(obj)

    def add_car(self, plate):
        if plate not in self.plates:
            self.plates.append(plate)
            self.update_displays()

    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()

    def update_displays(self):
        for display in self.displays:
            display.update()

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

#            # ... inside the register method
#    if isinstance(component, Sensor):
#       self.sensors.append(component)

#    # TODO: (optional) add an elif to check if the component is a Display - MUST

        if isinstance(component, Sensor):
            self.sensors.append(component)

        elif isinstance(component, Display):
            self.displays.append(component)

#    # ... inside the CarPark class
#    def register(self, component):
#       if not isinstance(component, (Sensor, Display)):
#          raise TypeError("Object must be a Sensor or Display")