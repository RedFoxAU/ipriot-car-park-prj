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