class Vehicle(object):
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100


    def emptyTank(self):
        self.gas = 0


    def gasLeft(self):
        return self.gas    
    

class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print("Beep beep")


class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires

    def beep(self):
        print("Honk honk")


my_car = Car(price=20000, gas=50, color="red", speed=150)

print(my_car.color)   # red
print(my_car.gasLeft())  # 50
my_car.beep()        # Beep beep
my_car.fillUpTank()
print(my_car.gasLeft())  # 100


my_truck = Truck(price=35000, gas=30, color="blue", tires=6)

print(my_truck.color)    # blue
print(my_truck.tires)    # 6
my_truck.beep()          # Honk honk
my_truck.emptyTank()
print(my_truck.gasLeft()) # 0
