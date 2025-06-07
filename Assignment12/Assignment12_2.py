class Circle():
    PI = 3.144

    def __init__ (self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter radius of circle : "))

    def calculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def calculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def display(self):
        print("Radius of Circle is : ", self.Radius)
        print("Area of Circle : ", self.Area)
        print("Circumference of Circle : ", self.Circumference)

circle1 = Circle()
circle1.Accept()
circle1.calculateArea()
circle1.calculateCircumference()
circle1.display()

print()

circle2 = Circle()
circle2.Accept()
circle2.calculateArea()
circle2.calculateCircumference()
circle2.display()