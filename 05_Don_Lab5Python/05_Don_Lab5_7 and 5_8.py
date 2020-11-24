class Vehicle:
    pass

class Vehicle:
    engine_capacity = "1,6 Turbo"

class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
       self.number_of_wheels = number_of_wheels
       self.type_of_tank = type_of_tank
       self.seating_capacity = seating_capacity
       self.maximum_velocity = maximum_velocity

    def drive(self):
        print("This " + self.type_of_tank + " can go up to a maximum speed of " + str(self.maximum_velocity) +" Km/h")

vios = Vehicle('4','petrol',5,180)
print(vios.number_of_wheels)
print(vios.type_of_tank)
print(vios.seating_capacity)
print(vios.maximum_velocity)

vios.drive()

class ElectricCar(Vehicle):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Vehicle.__init__(self, number_of_wheels, 'electric', seating_capacity, maximum_velocity)

blueSG = ElectricCar ('4', 5, 150)
print(blueSG.number_of_wheels)
print(blueSG.type_of_tank)
print(blueSG.seating_capacity)
print(blueSG.maximum_velocity)
blueSG.drive()