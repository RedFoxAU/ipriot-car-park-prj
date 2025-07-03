from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display
from pathlib import Path

def main():
    """
    Initializes the Car Park system, simulates vehicle entry and exit,
    and displays status messages.
    """
    car_park = CarPark(location="Moondalup", capacity=100, log_file=Path("moondalup.txt"))
    car_park.write_config("moondalup_config.json")
    car_park = CarPark.from_config("moondalup_config.json")

    entry_sensor = EntrySensor(id=1, is_active=True, car_park=car_park)
    exit_sensor = ExitSensor(id=2, is_active=True, car_park=car_park)
    display1 = Display(id=1, message="Welcome to Moondalup - 1SPACE-LEFT Car Parks!", is_on=True)
    print(f"{display1}")

    # Simulation of Ten Cars entering Car Park.
    for i in range(10):
        entry_sensor.detect_vehicle()
        print("Available bays:", car_park.available_bays)

    # Simulation of Two cars exiting Car Park.
    exit_sensor.detect_vehicle()  # One Car Exits
    print("Available bays:", car_park.available_bays)
    print("Cars remaining in Car Park", car_park.plates)
    exit_sensor.detect_vehicle()  # Second Car Exits
    print("Available bays:", car_park.available_bays)
    print("Cars remaining in Car Park", car_park.plates)

if __name__ == "__main__":
    main()
