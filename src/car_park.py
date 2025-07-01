class CarPark:
    def __init__(self, location="Unknown", capacity=0, plates=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."

    def car_entered(self, license_plate):
        print(f"Car entered with plate: {license_plate}")

    def car_exited(self, license_plate):
        print(f"Car exited with plate: {license_plate}")

    def register(self, obj):
        if isinstance(obj, Display):
            self.displays.append(obj)
        # If you want to register sensors, add here too (optional)

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