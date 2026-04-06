#Nick Kintigh
#April 6th 2026
#Module 3 Lab

#superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

#automobile class, inherits from vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        Vehicle.__init__(self, vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("Here is your car:")
        print("Vehicle type: " + self.vehicle_type)
        print("Year: " + self.year)
        print("Make: " + self.make)
        print("Model: " + self.model)
        print("Doors: " + self.doors)
        print("Roof: " + self.roof)

vehicle_type = "car"

print("Enter your car info:")
year = input("Year: ")
make = input("Make: ")
model = input("Model: ")
doors = input("Doors (2 or 4): ")
roof = input("Roof type (solid or sun roof): ")

my_car = Automobile(vehicle_type, year, make, model, doors, roof)
my_car.display_info()
