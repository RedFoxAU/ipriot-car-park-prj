from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

def main():
# TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"



# TODO: Write the car park configuration to a file called "moondalup_config.json"


# TODO: Reinitialize the car park object from the "moondalup_config.json" file


# TODO: create an entry sensor object with id 1, is_active True, and car_park car_park


# TODO: create an exit sensor object with id 2, is_active True, and car_park car_park


# TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park


# TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)


# TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)



    # Create display
    display1 = Display(id=1, message="Welcome to Moondalup Car Park", is_on=True)

    # Create car park
    car_park = CarPark(location="Moondalup Central", capacity=5, displays=[display1])

    # Create sensor
    sensor1 = Sensor(sensor_id=101, bay_id=1)
    #print(sensor1)

    print(car_park)

    # Simulate car entry
    car_park.car_entered("ABC123")

    # Simulate car exit
    car_park.car_exited("ABC123")

if __name__ == "__main__":
    main()
