from car_park import CarPark
from sensor import Sensor
from display import Display

def main():
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
