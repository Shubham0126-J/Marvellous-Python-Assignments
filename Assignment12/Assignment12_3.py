class Arithmatic():

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first Number : "))
        self.Value2 = int(input("Enter Second Number : "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Substraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 != 0:
            return self.Value1/self.Value2
        else:
            return "Error : Division by Zero" 

    
print("Operation for Object 1: ")
obj1 = Arithmatic()
obj1.Accept()
print("Addition of Entered Number is : ", obj1.Addition())
print("Substraction of Entered Number is : ", obj1.Substraction())
print("Multiplication of Entered Number is : ", obj1.Multiplication())
print("Dividion of Entered Number is : ", obj1.Division())

print()

print("Operation for Object 2: ")
obj2 = Arithmatic()
obj2.Accept()
print("Addition of Entered Number is : ", obj2.Addition())
print("Substraction of Entered Number is : ", obj2.Substraction())
print("Multiplication of Entered Number is : ", obj2.Multiplication())
print("Division of Entered Number is : ", obj2.Division())