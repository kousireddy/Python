class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive!")
        
class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("sail!")
        
class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!")

car1 = car("Ford","Mustang")            #create a car object
boat1 = Boat("Ibiza","Touring 20")      #create a boat object
plane1 = Plane("Boeing","747")          #create a plane object

for x in (car1,boat1,plane1):
    x.move()
