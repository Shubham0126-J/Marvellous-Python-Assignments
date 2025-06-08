class Rectangle:
    def __init__(self, length, width):
        self.Length = length
        self.Width = width

    def Area(self):
        return self.Length * self.Width

    def Perimeter(self):
        return 2 * (self.Length + self.Width)
        
    def display(self):
        print(f"Area of Rectangle :{self.Area()}, Perimeter of Rectangle: {self.Perimeter()}")

ret1 = Rectangle(50, 30)

ret1.display()