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
