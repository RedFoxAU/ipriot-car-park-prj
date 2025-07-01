class Sensor:
    def __init__(self, sensor_id, bay_id, occupied=False):
        self.sensor_id = sensor_id
        self.bay_id = bay_id
        self.occupied = occupied

    def __str__(self):
        status = "Occupied" if self.occupied else "Available"
        return f"Sensor {self.sensor_id} monitoring bay {self.bay_id}: {status}"
