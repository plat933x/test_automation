class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    def upper_name(self):
        return self.name.upper()

    def mileage_correction(self):
        return self.mileage - 150000

# class Bus inherits from class Vehicle
class Bus(Vehicle):
    pass

test_object = Bus("Benz Bus", 1500000, 100)
print("Name of our school bus is", test_object.upper_name())
print("Actual mileage of the car for buyers is:", test_object.mileage_correction())

second_bus = Bus("Skoda Bus", 500000, 250)
print("Total Bus fare is:", second_bus.fare())

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("DRIVE A CAR!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("SAIL A BOAT!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("FLY A PLANE!")

car_1 = Car("Mitsubishi", "ASX")
boat_1 = Boat("Argonaut", "C720")
plane_1 = Plane("Boeing", 737)

# Look at the for loop at the end. Because of polymorphism we can
# execute the same method for all three classes.
for i in (car_1, boat_1, plane_1):
    print(i.brand, i.model)
    i.move()