| Class Name | Attributes                                      | Methods                                                                 |
|------------|-------------------------------------------------|-------------------------------------------------------------------------|
| CarPark    | name, capacity, plates, sensors, displays, log_file, weather | add_car(), remove_car(), update_displays(), car_entered(), car_exited(), available_bays() |
| Sensor     | sensor_id, bay_id, occupied, car_park           | detect_car_entry(), detect_car_exit(), is_occupied(), _scan_plate() |
| Display    | display_id, message, is_on                      | update(), update_message(), turn_on()                       |
