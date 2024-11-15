class Vehicle:
    def __init__(self, name, milage, capacity):
        self.name = name
        self.milage = milage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 10
    
class Taxi(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10/100
        return amount

taxi_car = Taxi("BMW", 20, 50)
print("Total fare", taxi_car.fare())
