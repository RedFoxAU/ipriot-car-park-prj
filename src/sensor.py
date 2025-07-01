class Sensor:
    def __init__(self, sensor_id, bay_id, occupied=False):
        self.sensor_id = sensor_id
        self.bay_id = bay_id
        self.occupied = occupied

    def __str__(self):
        status = "Occupied" if self.occupied else "Available"
        return f"Sensor {self.sensor_id} monitoring bay {self.bay_id}: {status}"

    def detect_car_entry(self, license_plate):
        pass

    def detect_car_exit(self):
        pass


# class Sensor:
#     def __init__(self, id ...): # Add the other parameters
#         self.id = id
#         self.is_active = is_active
#         ... # Add the other attributes

#     def __str__(self):
#         ... # Return a string containing the sensor's id and status

# class EntrySensor(Sensor):
#     ...

# # Also create an ExitSensor class

class Sensor:
    def __init__(self, car_park):
        self.car_park = car_park

    def detect_car(self):
        pass  # To be implemented in subclasses

    def update_car_park(self, plate):
        pass  # To be implemented in subclasses


class EntrySensor(Sensor):
    def detect_car(self):
        # Simulate detecting a car entering
        plate = self.scan_plate()
        self.update_car_park(plate)

    def scan_plate(self):
        # Simulated plate detection
        return "ABC123"

    def update_car_park(self, plate):
        self.car_park.add_car(plate)


class ExitSensor(Sensor):
    def detect_car(self):
        plate = self.scan_plate()
        self.update_car_park(plate)

    def scan_plate(self):
        return "ABC123"

    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
