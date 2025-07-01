class Display:
    def __init__(self, id, message="", is_on=False):
        self.id = id
        self.message = message
        self.is_on = is_on

    def __str__(self):
        return f"Display {self.id}: {self.message}"

    def update_message(self, message):
        self.message = message

    def turn_on(self):
        self.is_on = True

    def update(self, data):
        if "message" in data:
            self.update_message(data["message"])

        for key, value in data.items():
            print(f"{key}: {value}")





        # if self.is_on:
        #     print(f"Display {self.id}: {self.message}")
        # else:
        #     print(f"Display {self.id} is off.")

    # def update(self):
    #     self.message = f"Display {self.id}: {len(self.car_park.plates)} cars in the car park."