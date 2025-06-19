class Vehicle:
    def __init__(self,brand,model):
        self.b = brand
        self.m = model
    def move(self):
        print("Drive!")

class car(Vehicle):
    pass

class boat(Vehicle):
    def move(self):
        print("sail!")

class plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = car("Ford", "Mustang")       #Create a Car object
boat1 = boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = plane("Boeing", "747")     #Create a Plane object

for x in (car1,boat1,plane1):
    print(x.b)
    print(x.m)
    x.move()
