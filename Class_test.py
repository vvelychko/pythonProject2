class Vehicle:
    def __init__(self):
        self.tank = 800
        self.fuel = 700

    def drive(self):
        print(f"I driving somewhere")
        self.tank -= 50

    def refuel(self, fuel_amount):
        if self.fuel + fuel_amount <= self.tank:
            print("I'm refueled")
        else:
            print('To much Fuel!')


class LandVehicle(Vehicle):
    pass

class WaterVehicle(Vehicle):
    pass


class WheeledVehicle(LandVehicle):
    def __init__(self):
        super().__init__()
        self.number = None

    def number_wheels(self, number):
        self.number = number
        if self.number == 4:
            print("This is a car")
            if self.number == 3:
                print("This is a sidecar motorcycle")
                if self.number == 2:
                    print("This is a bike")
                    if self.number == 1:
                        print("This is a monowheel")


class TrackedVehicle(LandVehicle):
    pass