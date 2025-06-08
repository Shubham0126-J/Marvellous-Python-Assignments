class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car Engine started.")
        print("Seatbelt check done.")
        print("Music system is ON.")

v = Vehicle()
v.start()
print()
c= Car()
c.start()