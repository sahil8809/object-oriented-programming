class Vehicle:
    def drive(self):
        print("Vehicle is moving")

class Car(Vehicle): #inheritence
    def ac(self):
        print("AC is on")
c1 = Car()
c1.drive()             
c1.ac() 